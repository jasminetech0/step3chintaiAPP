# shareinfo_.py
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# .envファイルから環境変数をロード
load_dotenv()

def send_email(subject, body, to_email):
    from_email = os.getenv('from_email')  # .envファイルから送信元メールアドレスを取得
    from_password = os.getenv('EMAIL_PASSWORD')  # .envファイルからパスワードを取得

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.close()
        return "Email sent successfully!"
    except Exception as e:
        return str(e)

# サンプルデータ
selected_realestates = [
    ["https://suumo.jp/chintai/jnc_000090614568/?bc=100381210517", "東京都文京区音羽１", 35.713969, 139.729924, "3LDK", 288000, 288000, 288000, 11, 67.01, "江戸川橋駅", 3, "https://img01.suumo.com/front/gazo/fr/bukken/517/100381210517/100381210517_ct.jpg"],
    ["https://suumo.jp/chintai/jnc_000090614522/?bc=100377064745", "東京都中央区晴海１", 35.659374, 139.784535,"1LDK", 200000, 200000, 200000, 27, 53.98, "月島駅", 7, "https://img01.suumo.com/front/gazo/fr/bukken/745/100377064745/100377064745_ct.jpg"],
    ["https://suumo.jp/chintai/jnc_000090678356/?bc=100381740081", "東京都渋谷区神宮前４", 35.668067, 139.70917,"3LDK", 1005000, 3015000, 1005000, 12, 134, "明治神宮前駅", 4, "https://img01.suumo.com/front/gazo/fr/bukken/081/100381740081/100381740081_ct.jpg"],
    ["https://suumo.jp/chintai/jnc_000090401259/?bc=100379530385", "東京都港区海岸１", 35.653929, 139.761254,"1LDK", 200000, 200000, 400000, 21, 51.39, "大門駅", 3, "https://img01.suumo.com/front/gazo/fr/bukken/385/100379530385/100379530385_ct.jpg"],
    ["https://suumo.jp/chintai/jnc_000090266928/?bc=100379015038", "東京都渋谷区千駄ヶ谷３", 35.676054, 139.706086, "1LDK", 200000, 200000, 0, 20, 37.99, "原宿駅", 4, "https://img01.suumo.com/front/gazo/fr/bukken/038/100379015038/100379015038_ct.jpg"]
]

# データを文字列形式に変換
selected_realestates_str = [
    f"URL: {item[0]}, 住所: {item[1]}, 間取り: {item[4]}, 賃料: {item[5]}, 敷金: {item[6]}, 礼金: {item[7]}, 最寄り駅: {item[10]}, 駅からの距離: {item[11]}分"
    for item in selected_realestates
]



def shareinfo(selected_realestates, to_email):
    if selected_realestates and to_email:
        subject = "Selected Real Estates"
        body = "\n".join(selected_realestates)
        result = send_email(subject, body, to_email)
        return result
    else:
        return 'Please select real estates and provide a recipient email!'
    






