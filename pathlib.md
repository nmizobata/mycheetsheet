# Pathlib メモ
## import文
`from pathlib import Path`  pathlibをインポートする

## パス情報の取得
`pathobj = Path(".")`  現ディレクトリのPathオブジェクトを得る
`Path("/a/a/a/").cwd()` Pathオブジェクトの内容に関係なく、現在のディレクトリを得る
`pathobj.iterdir()` 現ディレクトリ内のファイルやディレクトリを得る(iterdir()はイテレータオブジェクトなので、リスト化する必要がある)
```
files_and_dirs_itr = p.iterdir()
for file_and_dir in files_and_dirs_itr:
    print("現ディレクトリの中身:{}".format(file_and_dir))
``` 
`pathobj.rglob()` ワイルドカード検索→イテレータオブジェクト 現ディレクトリだけでなくサブディレクトリのものも検出する。
`pathobj.glob()` ワイルドカード検索→イテレータオプジェクト 現ディレクトリだけで検出する。
```
files_py = pathobj.rglob("*.py")
for file_py in files_py:
    print("現ディレクトリの.pyファイル:{}".format(file_py))
```


## パス情報の操作 (実ファイル/フォルダの変更は行わず情報の操作のみ)
p = Path(c:hoge/hoge2/hoge3.txt)
`p.parent` c:hoge/hoge2  
`p.parent.parent`  c:hoge  
`p.parent.parent.parent` c:  
`p.parent.parent.parent.parent` c: ドライブまで達したらドライブ名のみを返す  
`p.with_suffix(".hoge")` c:hoge/hoge2/hoge3.hoge 拡張子情報の変更 = p.parent / (p.stem + ".hoge")
`p.with_name("hoge999.txt")`c:hoge/hoge2/hoge999.txt ファイル名情報の変更 = p.parent / "hoge999.txt"
`p.with_stem("hogehoge")` c:hoge/hoge2/hogehoge.txt 拡張子除くファイル名の変更 = p.parent / "hogehoge"+p.suffix
`p / "hogehoge"` c:hoge\hoge2\hoge3.txt\hogehoge 子ディレクトリの追加  
`p.drive` c:  
`p.name`  hoge3.txt  ファイル名  
`p.stem`  hoge  拡張子除くファイル名  
`p.suffix`  .txt 拡張子(.が付く)  
`p.parts`   ('c:', 'hoge', 'hoge2', 'hoge3.txt')  パスの各パーツを分離  
`text = p.absolute()` 現ディレクトリの絶対パスの文字列を得る
`text = p.resolve()` 現ディレクトリの絶対パスの文字列を得る

## 実ディレクトリに対する操作
### ファイルの作成/削除
p = Path("c:hoge/hoge2/hoge3.txt")
`p.touch()`  hoge3.txtという空のファイルを作成する。既存の場合はタイムスタンプを更新。
親ディレクトがないとエラー。`p.parent.mkdir(parents=True, exist_ok=True)`をまず実行する。  
`p.touch(exist_ok=False)`  既存のファイルがある場合はエラーになる  
`p.unlink()`  ファイルの削除。ファイルが存在しない場合はエラー。ディレクトリもエラー。  
`p.unlink(missing_ok=True)`  ファイルが存在しない場合でもエラーにならない。  

### ディレクトリ作成/削除
p = Path("c:hoge/hoge2")
`p.mkdir()`  パスの作成。親ディレクトリ(c:hoge)がない時、すでにディレクトリが存在している場合エラー。  
`p.mkdir(parents=True)`  親ディレクトリ(c:hoge)が無くても、c:hogeを作ってhoge2ディレクトリを作成。  
`p.mkdir(exist_ok=True)` すでにディレクトリが存在していてもエラーにならない。(ディレクトリではなくファイルの場合はエラーになる)  
`p.parent.mkdir(parents=True, exist_ok=True)`  親ディレクトリが無くても作成。すでにディレクトリがあってもエラーにならない。  
`p.rmdir()`  パスの削除。中身が空の場合のみ。中身がある場合はエラーになる。  
丸ごと削除する場合は`shutil.rmtree(pathobj)`を使う。  

### 名前の変更
p = Path("c:hoge/hoge2/hoge3.txt")
注意: 絶対パス情報を使うこと。ファイル名だけ、フォルダ名だけ、で実行すると、新しい名前でPython実行ファイルのルートに保存される。
`p.rename(p.parent / "gegege.txt")`  "c:hoge/hoge2/gegege.txt"に名前を変更
`p.parent.rename(p.parent.parent / "gege")` "c:hoge/gege/" フォルダにファイルがあってもフォルダ名を変更可
`p.rename(p.parent / "test" / p.name)` "c:hoge/test/hoge3.txt"へファイルを移動。("test"フォルダが存在していること)
注意: ファイルのコピー機能は存在しない。shutilを使うこと。

## ファイルテキスト読み取り書き込み
読み込み
```
with pathobj.open(mode='r') as f:  mode='r'は省略可。
    text = f.read()
```
```
pathobj.read_text()    ファイル全体を読み込み
```
書き込み
```
with pathobj.open(mode='w') as f:
    f.write(text)
```
```
pathobj.write_text(text)    textを書き込み。同名のファイルがある場合は上書きされる。   
```
## 活用例
##### Path(\_\_file\_\_)を基準にファイル操作すると、自分のファイルを基準にファイルアクセスができる
hoge/hoge1/hoge_current.txtから、hoge/hoge2/hoge3.txtを相対パスで指定する
```
Path(__file__).parent.parent / hoge2 / hoge3.txt
```
##### ファイル名の拡張子直前に'_new'を付加したパス情報を取得
```
oldPath = Path("c:hoge/hoge2/hoge3.txt")
newPath = oldPath.parent / "{}_new{}".format(oldPath.stem,oldPath.suffix)
newPath = oldPath.with_stem("{}_new".format(oldPath.stem))
```
##### ファイルが存在するか
```
path_text = "c:hoge/hoge2/hoge3.txt"
Path(path_text).exists()
```
##### サブディレクトのみを取り出したい場合はリスト内表記で条件付けする
```
for dirname in [x for x in p.iterdir() if x.is_dir()]:
    print("現ディレクトリのサブディレクトリ:{}".format(dirname))
```
##### ファイルのみを取り出したい場合はリスト内表記で条件付けする
```
for filename in [x for x in p.iterdir() if x.is_file()]:
    print("現ディレクトリのファイル:{}".format(filename))
```
##### シンボリックファイル
その他、symboolicfile等の条件式あり。

##### 一覧からすべてのファイルを削除
```
for p in p_dir.iterdir():
    if p.is_file():
        p.unlink()
```
```
[p.unlink() for p in p_dir.iterdir() if p.is_fiule()]
```

### 注意
- ファイル名を弄る場合(文字列計算をする場合)はカッコでくくること。
`new_filename = Path(path_text).parent / (Path(path_text).stem+"_new"+Path(path_text).suffix)`



