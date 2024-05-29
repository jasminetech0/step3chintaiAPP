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
import sqlite3
import pandas as pd

def make_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def account_registration():
    st.write(f"### 新規ユーザ登録")

    # 登録用のフォーム
    with st.form("registration_form"):
        columns = ["username", "user_mail_address", "password", "share_mail_address", "favorite_place1_name", "fovorite_place1_address",
                   "favorite_place2_name", "fovorite_place2_address", "favorite_place3_name", "fovorite_place3_address", "favorite_place4_name", "fovorite_place4_address"]
        username = st.text_input("ユーザー名(必須)")
        user_mail_address = st.text_input("メールアドレス(必須)")
        password = make_hash(st.text_input("パスワード(必須)", type="password"))
        share_mail_address = st.text_input("共有先メールアドレス")
        favorite_place1_name = st.text_input("お気に入り地点１")
        favorite_place1_address = st.text_input("お気に入り地点１ 住所")
        favorite_place2_name = st.text_input("お気に入り地点２")
        favorite_place2_address = st.text_input("お気に入り地点２ 住所")
        favorite_place3_name = st.text_input("お気に入り地点３")
        favorite_place3_address = st.text_input("お気に入り地点３ 住所")
        favorite_place4_name = st.text_input("お気に入り地点４")
        favorite_place4_address = st.text_input("お気に入り地点４ 住所")
        submitted = st.form_submit_button("登録")
     
        # 登録ボタンを押すとDBへ情報を登録する
        if submitted and (username != "" and user_mail_address != "" and password != ""):
            tmp = [[username, user_mail_address, password, share_mail_address, favorite_place1_name, favorite_place1_address,
                favorite_place2_name, favorite_place2_address, favorite_place3_name, favorite_place3_address, favorite_place4_name, favorite_place4_address]]
            df_user = pd.DataFrame(tmp, columns=columns)
            with sqlite3.connect('./user.db') as conn:
                df_user.to_sql('users', conn, if_exists="append", index=False)
            st.toast("登録完了！")
        else:
            st.warning("必須項目を入力してください。")
            submitted = False
