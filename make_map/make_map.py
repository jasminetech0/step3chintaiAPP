import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# エリアの選択肢
areas = ["千代田区", "中央区", "港区", "渋谷区", "新宿区", "文京区"]
# 間取りの選択肢
layouts = ["1LDK", "2K~2LDK", "3K~3LDK"]

# サイドバーに各種条件を設定
st.sidebar.markdown("## 🏢エリア")
selected_areas = [area for area in areas if st.sidebar.checkbox(area, key=area)]

st.sidebar.markdown("## 💰賃料")
min_rent, max_rent = st.sidebar.slider(
    "賃料の範囲を選択してください",
    min_value=100000,
    max_value=300000,
    value=(100000, 300000),
    step=10000
)

st.write(f"選択された賃料範囲: {min_rent}円 〜 {max_rent}円")

st.sidebar.markdown("## 🏠間取り")
selected_layouts = [layout for layout in layouts if st.sidebar.checkbox(layout, key=layout)]

# 間取りのフィルタリングを適用
layout_mapping = {
    "1LDK": ["1LDK"],
    "2K~2LDK": ["2K", "2LDK"],
    "3K~3LDK": ["3K", "3LDK"]
}
selected_layouts_flat = [item for sublist in [layout_mapping[layout] for layout in selected_layouts] for item in sublist]

# 検索ボタン
if st.sidebar.button("検索"):
    # CSVファイルの読み込み
    df = pd.read_csv('C:/Users/jiebing/Desktop/ChintaiAPP/make_db/tokyo6ku_cleaned.csv')

    # データのフィルタリング
    filtered_df = df[
        (df['エリア'].isin(selected_areas)) &
        (df['賃料'] >= min_rent) &
        (df['賃料'] <= max_rent) &
        (df['間取り'].isin(selected_layouts_flat))
    ]

    # フィルタリング結果の表示
    st.write(f"検索結果: {len(filtered_df)}件")
    st.dataframe(filtered_df)  # ここでst.dataframeを使用してインタラクティブなテーブルを表示

    # 地図の作成
    if not filtered_df.empty:
        m = folium.Map(location=[filtered_df['緯度'].mean(), filtered_df['経度'].mean()], zoom_start=12)

        # マーカーの追加
        for idx, row in filtered_df.iterrows():
            folium.Marker(
                location=[row['緯度'], row['経度']], 
                popup=f"{row['物件名']} - 賃料: {row['賃料']}円 - 間取り: {row['間取り']}",
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)

        # 地図の表示
        folium_static(m)
    else:
        st.write("該当する物件は見つかりませんでした。")
