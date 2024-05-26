#############
#【関数名】
# 物件検索（realestate_search）
#【処理内容】
# 入力された検索条件に合う物件を抽出し、物件リストを返す

#【入力パラメータ】 *暫定
# ・エリア：list,str
# ・最低賃料：int
# ・最高賃料：int
# ・間取り：list,str
# etc....
#【返り値】
# ・物件リスト：dataframe
#############

import pandas as pd
import streamlit as st

def realestate_search(selected_areas, min_rent, max_rent, selected_layouts_flat):
    # # 空のデータフレームを定義するための列名。項目は適当なので適宜修正。間取り図取るのは難しいかも？
    # # 住所から緯度経度に直す処理が必要。国土地理院APIやgeocodingスクレイピングでできそう。
    # columns = ['url', 'address', 'latitude', 'longitude', 'house_layout', 'rent','deposit', 'gratuity_fee', 'years', 'occupied_area', 'nearest_station', 'required_time', 'floor_plan']
    # # 追加するサンプルデータ
    # sample_data = [
    #     ["https://suumo.jp/chintai/jnc_000090614568/?bc=100381210517", "東京都文京区音羽１", 35.713969, 139.729924, "3LDK", 288000, 288000, 288000, 11, 67.01, "江戸川橋駅", 3, "https://img01.suumo.com/front/gazo/fr/bukken/517/100381210517/100381210517_ct.jpg"],
    #     ["https://suumo.jp/chintai/jnc_000090614522/?bc=100377064745", "東京都中央区晴海１",  35.659374, 139.784535,"1LDK", 200000, 200000, 200000, 27, 53.98, "月島駅", 7, "https://img01.suumo.com/front/gazo/fr/bukken/745/100377064745/100377064745_ct.jpg"],
    #     ["https://suumo.jp/chintai/jnc_000090678356/?bc=100381740081", "東京都渋谷区神宮前４", 35.668067, 139.70917,"3LDK", 1005000, 3015000, 1005000, 12, 134, "明治神宮前駅", 4, "https://img01.suumo.com/front/gazo/fr/bukken/081/100381740081/100381740081_ct.jpg"],
    #     ["https://suumo.jp/chintai/jnc_000090401259/?bc=100379530385", "東京都港区海岸１", 35.653929, 139.761254,"1LDK", 200000, 200000, 400000, 21, 51.39, "大門駅", 3, "https://img01.suumo.com/front/gazo/fr/bukken/385/100379530385/100379530385_ct.jpg"],
    #     ["https://suumo.jp/chintai/jnc_000090266928/?bc=100379015038", "東京都渋谷区千駄ヶ谷３", 35.676054, 139.706086, "1LDK", 200000, 200000, 0, 20, 37.99, "原宿駅", 4, "https://img01.suumo.com/front/gazo/fr/bukken/038/100379015038/100379015038_ct.jpg"]
    #     ]
    # # サンプルデータをデータフレームに追加
    # df_realestates = pd.DataFrame(sample_data, columns=columns)


    # CSVファイルの読み込み
    df = pd.read_csv('./make_db/tokyo6ku_cleaned.csv')

    # データのフィルタリング
    filtered_df = df[
        (df['エリア'].isin(selected_areas)) &
        (df['賃料'] >= min_rent) &
        (df['賃料'] <= max_rent) &
        (df['間取り'].isin(selected_layouts_flat))
    ]

    
    filtered_df["check"] = False
    # filtered_df["check"].fillna(False)
    # st.data_editor(filtered_df, disabled=disabled)
    # st.dataframe(filtered_df)  # ここでst.dataframeを使用してインタラクティブなテーブルを表示
    return filtered_df