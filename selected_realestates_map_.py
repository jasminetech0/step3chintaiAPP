#############
#【関数名】
# マップ表示（selected_realestates_map）
#【処理内容】
# 物件リストを地図上に表示し、地図上で選択した物件のリストを返す

#【入力パラメータ】
# ・物件リスト:dataframe
#【返り値】
# ・選択物件リスト：dataframe
#############
import streamlit as st
import pandas as pd
import folium

def selected_realestates_map(df_realestates):
    st.map(df_realestates[["latitude", "longitude"]])
    df_selected_realestates = df_realestates
    return df_selected_realestates