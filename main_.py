# サブモジュールをインポート
from account_registration_ import account_registration
from login_ import login
from realestate_search_ import realestate_search
from make_map_ import make_map
from compare_realestates_ import compare_realestates

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
    areas = ["千代田区", "中央区", "港区", "渋谷区", "新宿区","文京区"]
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

    # 検索ボタンを押すとDBから検索条件に合う物件リストを返す
    if st.sidebar.button("検索"):
        st.session_state.df_realestates = realestate_search(selected_areas, min_rent, max_rent, selected_layouts_flat)

    # メイン画面
    if "df_realestates" in st.session_state:
        # 表示する列を定義
        displayed = ["エリア", "最寄り駅と距離", "賃料", "敷金", "礼金", "間取り", "築年数"]
        st.session_state.df_realestates["check"] = st.data_editor(st.session_state.df_realestates[["check"] + displayed], hide_index="bool",disabled=displayed)["check"]
        # インタラクティブなマップで選択した物件のリストが入るようにする
        st.session_state.df_selected_realestates = st.session_state.df_realestates[st.session_state.df_realestates["check"]==True]

        if "df_selected_realestates" in st.session_state:
            # 選択された物件のみをマップに表示
            if len(st.session_state.df_selected_realestates) > 0:
                make_map(st.session_state.df_selected_realestates[["物件名", "賃料", "間取り","緯度","経度"]])

            # st.write(f"#### 暫定でサンプルデータのままで表示。お気に入り地点からの時間算出の機能は別ファイルで作成予定")
            compare_realestates(st.session_state.df_selected_realestates)
            st.write(f"##### ここに相場比較を入れる。別ページにするかは要検討")
            if st.button("Share"):
                ##ここにシェア機能をつなげる
                # message = sendemail(subject, df_share, to_email)
                st.write(message)
    else:
        st.write(f"## ようこそ")
    

# ログインしたらメイン画面を呼び出す。
if st.session_state.account_register:
    st.session_state.account_register = account_registration()
elif st.session_state.login_status:
    main()
else:
    top()