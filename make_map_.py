import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def make_map(df_selected):
    # 地図の作成
    m = folium.Map(location=[df_selected['緯度'].mean(), df_selected['経度'].mean()], zoom_start=12)

    # マーカーの追加
    for idx, row in df_selected.iterrows():
        folium.Marker(
            location=[row['緯度'], row['経度']], 
            popup=f"{row['物件名']} - 賃料: {row['賃料']}円 - 間取り: {row['間取り']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    # 地図の表示
    folium_static(m)
