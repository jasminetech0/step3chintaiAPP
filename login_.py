#############
#【関数名】
# ログイン機能（login）
#【処理内容】
# 入力されたユーザー名とパスワードの組合せから、ログイン成否を返す

#【入力パラメータ】
# ・ユーザー名：str
# ・パスワード：str
#【返り値】
# ・ログイン成否：boolean
# ・(成功したら)該当するユーザー情報：dataframe
#############
import pandas as pd
import streamlit as st
import sqlite3
import hashlib

def make_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def check_hashes(password,hashed_text):
	if make_hash(password) == hashed_text:
		return hashed_text
	return False

def login_user(username,password):
    with sqlite3.connect('./user.db') as conn:
        cur = conn.cursor()
        cur.execute(f'SELECT password FROM users WHERE username ="{username}"')
        if cur.fetchall()[0][0] == password:
            sql = f'SELECT * FROM users'
            df_tmp = pd.read_sql(sql, conn).iloc[0]
            result = True
        else:
            df_tmp = pd.DataFrame()
            result = False
    return  result, df_tmp

def login(username, password):
    hashed_pwd = make_hash(password)
    result, df_user  = login_user(username, hashed_pwd)
    if result:
        login_judge = True
        # ユーザーDBの情報から認証した結果を返す
        # with sqlite3.connect('./user.db') as conn:
        #     sql = 'SELECT * FROM users WHERE username = ?' #, username
        # df_user = result
    else:
        login_judge = False
        # df_user = pd.DataFrame()

    ##### サンプルデータ用 #####
    # # 空のデータフレームを定義するための列名
    # columns = ['username', 'user_mail', 'share_mail_address','favorite1', 'favorite2', 'favorite3', 'favorite4']
    # # 追加するサンプルデータ
    # sample_data = [
    #     ["相沢毅", "aizawa@ggmail.com", "aizawawife@ggmail.com", "東京都千代田区丸の内二丁目3番1号", "東京都渋谷区1丁目17-1", "東京都大田区羽田空港3丁目3-2", ""]
    #     ]
    # # サンプルデータをデータフレームに追加
    # df_user = pd.DataFrame(sample_data, columns=columns)
    # # 実装前は仮でTrue
    # login_judge = True
	#############################
    return df_user ,login_judge