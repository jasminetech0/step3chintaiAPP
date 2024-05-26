#############
#【関数名】
# 物件比較表示機能（compare_realestates）
#【処理内容】
# 選択された物件データから比較表を作る

#【入力パラメータ】
# ・選択された物件データ：df_selected_realestates
#【返り値】
# ・特になし？streamlitで表示させるのみ？
# ・
#############
import streamlit as st
import pandas as pd

compared = ["物件名", "エリア", "最寄り駅と距離", "賃料", "敷金", "礼金", "間取り", "専有面積", "築年数", "イメージ画像"]

def compare_realestates(df_selected_realestates):
    df_selected_realestates.reset_index(inplace=True)
    n_cols = len(df_selected_realestates) + 1   # 比較物件の数+1
    number_cols = st.columns(n_cols)
    for i in range(1, n_cols):
        number_cols[i].write(str(i))
        
    for i in range(len(compared)):
        cols = st.columns(n_cols)
        cols[0].write(compared[i])
        for index, row in df_selected_realestates.iterrows():
            if compared[i] == "物件名":
                cols[index+1].page_link(row["URL"], label=f":blue[{row[compared[i]]}]")
            elif compared[i] == "イメージ画像":
                cols[index+1].image(row[compared[i]])
            else:
                cols[index+1].write(row[compared[i]])

    return 0