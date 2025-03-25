# Pandas DataFrameメモ
## 条件フィルタリング(例1)
- name列の値がindicatorname、key列の値がkeyであるDataFrame(df)のvalue列の値を取り出す。
- フィルタリングの返り値はDataFrame型であり、さらに列を指定した場合はSeries型。返り値が一つしかないことが分かっている場合、iloc[0]で値を取り出す。
- 例外処理：フィルタリングの結果、該当するデータがない場合が発生する可能性がある。安全性を高めるために、エラーをキャッチする処理を追加する。
```
try:
    value = df.loc[(df["name"] == indicatorname) & (df["key"] == key)]["value"].iloc[0]
    return value
except IndexError:
    return None  # データがない場合に適切な処理
```
## .locを使用せずに.queryメソッドを使用すると簡潔に記述できる(多少遅くなる)
```
value = df.loc[(df["name"] == indicatorname) & (df["key"] == key)]["value"].iloc[0]
value = df.query("name == @indicatorname and key == @key")["value"].iloc[0]
```
## indicatornameを**含む**行を抽出する
```
value = df.loc[(df["name"].str.contains(indicatorname)) & (df["key"] == key)]["value"].iloc[0]
```
大文字小文字を区別しない場合
```
value = df.loc[(df["name"].str.contains(indicatorname, case=False)) & (df["key"] == key)]["value"].iloc[0]
```
name列に欠損値(NaN)が含まれる場合
```
value = df.loc[(df["name"].str.contains(indicatorname, case=False, na=False)) & (df["key"] == key)]["value"].iloc[0]
```

## queryメソッドを使用した場合
```
value = df.query("name.str.contains(@indicatorname, case=False, na=False) and key == @key", engine='python')["value"].iloc[0]
```