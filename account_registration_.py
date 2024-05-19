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
    st.write("アカウント登録のUIを作る")

    if st.button("登録"):
        return