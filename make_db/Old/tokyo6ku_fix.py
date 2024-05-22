import pandas as pd

# 入力CSVファイルのパス
input_file = r'C:\Users\jiebing\Desktop\ChintaiAPP\make_db\tokyo6ku_1000pages_all_property.csv'
# 出力CSVファイルのパス
output_file = r'C:\Users\jiebing\Desktop\ChintaiAPP\make_db\tokyo6ku_fix.csv'

# CSVファイルを読み込む
df = pd.read_csv(input_file, encoding='UTF-8-SIG')

# 指定された区のリスト
target_districts = ["東京都千代田区", "東京都港区", "東京都中央区", "東京都渋谷区", "東京都新宿区"]

# 住所カラムに指定された区で始まる行のみを抽出
filtered_df = df[df['住所'].str.startswith(tuple(target_districts))]

# 住所の最後に「丁目」を追加
filtered_df['住所'] = filtered_df['住所'].apply(lambda x: x + '丁目' if '丁目' not in x else x)

# フィルタリング結果を新しいCSVファイルに保存
filtered_df.to_csv(output_file, index=False, encoding='UTF-8-SIG')

print(f"Filtered data saved to {output_file}")
