# display_rent_comparison_.py
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def display_rent_comparison(df_selected_realestates):
    # グラフのデフォルトフォント指定
    plt.rcParams['font.family'] = "DejaVu Sans"
    plt.rcParams['font.size'] = 18  # デフォルトフォントサイズを18に設定

    # CSVファイルの相対パス
    file_path = './make_db/tokyo6ku_cleaned.csv'

    # CSVファイルの読み込み
    df = pd.read_csv(file_path)

    # 選択されたエリアを取得
    selected_areas = df_selected_realestates['エリア'].unique().tolist()


    # 間取りの選択肢
    layouts = ["1K", "2K", "2LDK", "3K", "3LDK"]

    if selected_areas:
        st.write(f"選択されたエリア: {', '.join(selected_areas)}")

        num_selected_areas = len(selected_areas)
        rows = (num_selected_areas + 2) // 3  # 3列で表示するための行数を計算

        # エリアごとに賃料相場を計算し、グラフを表示
        fig, axs = plt.subplots(rows, 3, figsize=(24, 8 * rows))
        axs = axs.flatten()  # 1次元配列に変換

        for i, area in enumerate(selected_areas):
            area_df = df[df['エリア'] == area]
            avg_rent = area_df.groupby('間取り')['賃料'].mean().reindex(layouts).dropna().reset_index()

            ax = axs[i]
            ax.bar(avg_rent['間取り'], avg_rent['賃料'])
            ax.set_title('Average Rent Comparison')
            ax.set_xlabel('Room Size')
            ax.set_ylabel('Average Rent')
            ax.set_ylim(0, 320000)  # 縦軸の最大値を設定

        # 不要なサブプロットを非表示にする
        for j in range(i + 1, len(axs)):
            fig.delaxes(axs[j])

        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.write("エリアを選択してください。")
