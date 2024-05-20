# サブモジュールをインポート
from account_registration_ import account_registration
from login_ import login
from realestate_search_ import realestate_search

#ライブラリをインストール
import streamlit as st
import pandas as pd

# 起動時にログイン状態を示すフラグを生成
if "login_status" not in st.session_state:
    st.session_state.login_status = False

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
    # アカウント登録ボタンを押すと登録画面に遷移する
    if st.sidebar.button("アカウント登録"):
        top_image.empty()
        account_registration()

# メイン画面
def main():
    # エリアの選択肢
    areas = ["千代田区", "中央区", "港区", "渋谷区", "新宿区","文京区"]
    # 間取りの選択肢
    layouts = [ "1LDK", "2K~2LDK", "3K~3LDK"]

    # サイドバーに各種条件を設定
    st.sidebar.markdown("## 🏢エリア")
    selected_areas = [st.sidebar.checkbox(area, key=area) for area in areas]

    st.sidebar.markdown("## 💰賃料")
    min_rent = st.sidebar.number_input("最低賃料を入力してください", min_value=0)
    max_rent = st.sidebar.number_input("最高賃料を入力してください", min_value=min_rent)

    st.sidebar.markdown("## 🏠間取り")
    selected_layouts = [st.sidebar.checkbox(layout, key=layout) for layout in layouts]

    # 検索ボタンを押すと
    if st.sidebar.button("検索"):
        st.session_state.df_realestates = realestate_search(selected_areas, min_rent, max_rent, selected_layouts)

    # メイン画面
    if "df_realestates" in st.session_state:        
        # マップ表示～物件選択の動きを別ファイルにできるか？
        # インタラクティブなマップにする必要あり
        st.map(st.session_state.df_realestates[["latitude", "longitude"]])

        # インタラクティブなマップで選択した物件のリストが入るようにする
        st.session_state.df_selected_realestates = st.session_state.df_realestates

        if "df_selected_realestates" in st.session_state:
            st.write(f"#### 暫定でサンプルデータのままで表示。お気に入り地点からの時間算出の機能は別ファイルで作成予定")
            st.dataframe(st.session_state.df_selected_realestates)
            st.write(f"##### ここに相場比較を入れる。別ページにするかは要検討")
            st.button("Share")
    else:
        st.write(f"## ようこそ")
    

# ログインしたらメイン画面を呼び出す。
if st.session_state.login_status:
    main()
else:
    top()