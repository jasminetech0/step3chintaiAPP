#############
#【関数名】
# アカウント登録（account_registration）
#【処理内容】
# ・アカウント登録用のStreamlitのUI
# ・入力した情報をユーザーDBに登録する

#【入力パラメータ】
# 特になし
#【返り値】
# 特になし。登録完了したらログインページに戻る
#############

import streamlit as st

def account_registration():
    st.write(f"### 新規ユーザ登録")

    # 登録用のフォーム
    with st.form("registration_form"):
        username = st.text_input("お名前")
        user_mail_address = st.text_input("メールアドレス")
        share_mail_address = st.text_input("共有先メールアドレス")
        favorite_place1_name = st.text_input("お気に入り地点１")
        fovorite_place1_address = st.text_input("お気に入り地点１ 住所")
        favorite_place2_name = st.text_input("お気に入り地点２")
        fovorite_place2_address = st.text_input("お気に入り地点２ 住所")
        favorite_place3_name = st.text_input("お気に入り地点３")
        fovorite_place3_address = st.text_input("お気に入り地点３ 住所")
        favorite_place4_name = st.text_input("お気に入り地点４")
        fovorite_place4_address = st.text_input("お気に入り地点４ 住所")
        
        submitted = st.form_submit_button("登録")
        if submitted:
            st.write("登録完了")
            return