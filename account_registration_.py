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
import hashlib

def make_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def account_registration():
    st.write(f"### 新規ユーザ登録")

    # 登録用のフォーム
    with st.form("registration_form"):
        username = st.text_input("お名前(必須)")
        user_mail_address = st.text_input("メールアドレス(必須)")
        password = st.text_input("パスワード(必須)", type="password")
        share_mail_address = st.text_input("共有先メールアドレス")
        favorite_place1_name = st.text_input("お気に入り地点１")
        fovorite_place1_address = st.text_input("お気に入り地点１ 住所")
        favorite_place2_name = st.text_input("お気に入り地点２")
        fovorite_place2_address = st.text_input("お気に入り地点２ 住所")
        favorite_place3_name = st.text_input("お気に入り地点３")
        fovorite_place3_address = st.text_input("お気に入り地点３ 住所")
        favorite_place4_name = st.text_input("お気に入り地点４")
        fovorite_place4_address = st.text_input("お気に入り地点４ 住所")
        
        if username == "" or user_mail_address == "" or password == "":
            st.warning("必須項目を入力してください。")
        else:
            st.success("登録可能")
        
        submitted = st.form_submit_button("登録")
        if submitted:
            st.write("success")
            # if username == "a" or user_mail_address == "" or password == "":
            #     st.warning("必須項目を入力してください。")
            #     submitted = False
            # else:
            #     st.write("登録完了")
            #     return True