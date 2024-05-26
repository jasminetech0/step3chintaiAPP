# サブモジュールをインポート
from account_registration_ import account_registration
from login_ import login
from realestate_search_ import realestate_search
from selected_realestates_map_ import selected_realestates_map
from make_map_ import make_map
from shareinfo_ import shareinfo, selected_realestates_str  # 必要な関数とデータをインポート
from display_rent_comparison_ import display_rent_comparison

#ライブラリをインストール
import streamlit as st
import pandas as pd

# 起動時にログイン状態を示すフラグを生成
if "login_status" not in st.session_state:
    st.session_state.login_status = False

if "account_register" not in st.session_state:
    st.session_state.account_register = False

if "df_user" not in st.session_state:
    st.session_state.df_user = pd.DataFrame()

# トップページ(ログインページ)
def top():
    #タイトル
    top_image = st.empty()
    with top_image.container():
        st.title('（仮）不動産スマートセレクト')
        st.image("./picture/top_picture.png")
    username = st.sidebar.text_input("ユーザー名")
    password = st.sidebar.text_input("パスワード")
    # ログインが成功したらメイン画面に遷移する
    if st.sidebar.button("ログイン"):
        st.session_state.df_user, st.session_state.login_status = login(username, password)
        st.rerun()
    # アカウント登録ボタンを押すと登録画面に遷移する
    if st.sidebar.button("アカウント登録"):
        st.session_state.account_register = True
        st.rerun()

# メイン画面
def main():
    # エリアの選択肢
    areas = ["千代田区", "中央区", "港区", "渋谷区", "新宿区"]
    # 間取りの選択肢
    layouts = [ "1LDK", "2K~2LDK", "3K~3LDK"]

    # サイドバーに各種条件を設定
    st.sidebar.markdown("## 🏢エリア")
    selected_areas = [area for area in areas if st.sidebar.checkbox(area, key=area)]

    st.sidebar.markdown("## 💰賃料")
    min_rent, max_rent = st.sidebar.slider(
        "賃料の範囲を選択してください",
        min_value=100000,
        max_value=300000,
        value=(100000, 300000),
        step=10000
    )

    st.write(f"選択された賃料範囲: {min_rent}円 〜 {max_rent}円")

    st.sidebar.markdown("## 🏠間取り")
    selected_layouts = [layout for layout in layouts if st.sidebar.checkbox(layout, key=layout)]

    # 間取りのフィルタリングを適用
    layout_mapping = {
        "1LDK": ["1LDK"],
        "2K~2LDK": ["2K", "2LDK"],
        "3K~3LDK": ["3K", "3LDK"]
    }
    selected_layouts_flat = [item for sublist in [layout_mapping[layout] for layout in selected_layouts] for item in sublist]

    # 検索ボタンを押すと
    if st.sidebar.button("検索"):
        make_map(selected_areas, min_rent, max_rent, selected_layouts_flat)
        st.session_state.df_realestates = realestate_search(selected_areas, min_rent, max_rent, selected_layouts)

    # メイン画面
    if "df_realestates" in st.session_state:        
        # マップ表示～物件選択の動きを別ファイルにできるか？
        # インタラクティブなマップにする必要あり
        mapholder = st.empty()
        with mapholder.container():
            selected_realestates_map(st.session_state.df_realestates)
        # st.map(st.session_state.df_realestates[["latitude", "longitude"]])

        # インタラクティブなマップで選択した物件のリストが入るようにする
        st.session_state.df_selected_realestates = st.session_state.df_realestates

        if "df_selected_realestates" in st.session_state:
            st.write(f"#### 暫定でサンプルデータのままで表示。お気に入り地点からの時間算出の機能は別ファイルで作成予定")
            st.dataframe(st.session_state.df_selected_realestates)
            st.write(f"##### ここに相場比較を入れる。別ページにするかは要検討")

            # display_rent_comparison 関数を呼び出す
            display_rent_comparison()


            # シェアする物件を選択
            #Shareinfoのサンプルデータを読み込む(↓一旦下記コードをMark Down)
            # selected_indices = st.multiselect("シェアする物件を選択してください", st.session_state.df_selected_realestates.index)
            # selected_realestates = st.session_state.df_selected_realestates.loc[selected_indices, 'Url'].tolist()

            # メールアドレスの入力
            to_email = st.text_input("送信先メールアドレスを入力してください")  

            if st.button("Share"):
                ##ここにシェア機能をつなげる
                # message = sendemail(subject, df_share, to_email)
                if to_email:
                    message = shareinfo(selected_realestates_str, to_email)  # shareinfo_.py の shareinfo 関数を使用
                    st.write(message)
                else:
                    st.error("送信先メールアドレスを入力してください。")
             
    else:
        st.write(f"## ようこそ")
    

# ログインしたらメイン画面を呼び出す。
if st.session_state.account_register:
    st.session_state.account_register = account_registration()
elif st.session_state.login_status:
    main()
else:
    top()