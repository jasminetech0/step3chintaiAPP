#ライブラリをインストール
import streamlit as st

#タイトル
st.title('（仮）不動産スマートセレクト')

# エリアの選択肢
areas = ["千代田区", "中央区", "港区", "渋谷区", "新宿区","文京区"]

# 間取りの選択肢
layouts = [ "1LDK", "2K~2LDK", "3K~3LDK"]

# サイドバーに各種条件を設定
st.sidebar.markdown("## 🏢エリア")
selected_areas = [st.sidebar.checkbox(area, key=area) for area in areas]

st.sidebar.markdown("## 💰賃料")
min_rent = st.sidebar.number_input("最低賃料を入力してください", min_value=0)
max_rent = st.sidebar.number_input("最高賃料を入力してください", min_value=min_rent)

st.sidebar.markdown("## 🏠間取り")
selected_layouts = [st.sidebar.checkbox(layout, key=layout) for layout in layouts]

