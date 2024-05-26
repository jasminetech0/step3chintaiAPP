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
import sqlite3
import hashlib

def make_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def check_hashes(password,hashed_text):
	if make_hash(password) == hashed_text:
		return hashed_text
	return False

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def login(username, password):
    # 空のデータフレームを定義するための列名
    columns = ['username', 'user_mail', 'share_mail','favorite1', 'favorite2', 'favorite3', 'favorite4']
    # 追加するサンプルデータ
    sample_data = [
        ["相沢毅", "aizawa@ggmail.com", "aizawawife@ggmail.com", "東京都千代田区丸の内二丁目3番1号", "東京都渋谷区1丁目17-1", "東京都大田区羽田空港3丁目3-2", ""]
        ]
    # サンプルデータをデータフレームに追加
    df_user = pd.DataFrame(sample_data, columns=columns)
   
    # # ユーザーDBの情報から認証した結果を返す
    # with sqlite3.connect('./user.db') as conn:
	# 	sql = 'SELECT * FROM users WHERE username = ?' #, username
	# 	df_users_sql = pd.read_sql(sql, conn)


    #### 実装前は暫定でTrueを入れておく
    login_success = True

    return df_user ,login_success