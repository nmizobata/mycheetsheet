# Pathlib メモ
## import文
`from pathlib import Path`  pathlibをインポートする
## Pathのメソッド
`pathobj = Path(".")`  現ディレクトリのPathオブジェクトを得る
`pathobj.absolute()` 現ディレクトリの絶対パスの文字列を得る
`pathobj.resolve()` 現ディレクトリの絶対パスの文字列を得る
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
## ディレクトリ作成/削除
`pathobj.mkdir()`  パスの作成。親ディレクトリがない場合、すでにディレクトリが存在している場合エラー。  
`pathobj.mkdir(parents=True)`  親ディレクトリが無くても作成することができる  
`pathobj.mkdir(exist_ok=True)` すでにディレクトリが存在していてもエラーにならない。(ディレクトリではなくファイルの場合はエラーになる)  
`pathobj.parent.mkdir(parents=True, exist_ok=True)`  親ディレクトリまでを作成。すでにディレクトリがあってもエラーにならない。  
`pathobj.rmdir()`  パスの削除。中身が空の場合のみ。中身がある場合はエラーになる。  
丸ごと削除する場合は`shutil.rmtree(pathobj)`を使う。  
## ファイルの作成/削除
`pathobj.touch()`  空のファイルを作成する。既存の場合はタイムスタンプを更新。親ディレクトがないとエラー。  上記`pathobj.parent.mkdir(parents=True, exist_ok=True)`をまず実行する。  
`pathobj.touch(exist_ok=False)`  既存のファイルがある場合はエラーになる  
`pathobj.unlink()`  ファイルの削除。ファイルが存在しない場合はエラー。ディレクトリもエラー。  
`pathobj.unlink(missing_ok=True)`  ファイルが存在しない場合でもエラーにならない。  
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
##### ファイル名の拡張子直前に'_new'を付加したパス名を取得
```
path_txt = "c:hoge/hoge2/hoge3.txt"
newPath_txt = Path(path_txt).parent / "{}_new{}".format(Path(path_txt).stem,Path(path.txt).suffix
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

### Path操作
c:hoge/hoge2/hoge3.txt  
`Path(path_text).parent` c:hoge/hoge2  
`Path(path_text).parent.parent`  c:hoge  
`Path(path_text).parent.parent.parent` c:  
`Path(path_text).parent.parent.parent.parent` c: ドライブまで達したらドライブ名のみを返す  
`Path(path_text).with_suffix(".hoge")` c:hoge/hoge2/hoge3.hoge 拡張子の置き換え(txt->hoge)  
`Path(path_text).with_name("hoge999.txt")`c:hoge/hoge2/hoge999.txt ファイル名の置き換え (hoge3->hoge999)  
`Path(path_text) / "hogehoge.txt"` c:hoge\hoge2\hoge3.txt\hogehoge.txt 子ディレクトリの追加  
`Path(path_text).drive` c:  
`Path(path_text).name`  hoge3.txt  ファイル名  
`Path(path_text).stem`  hoge  拡張子除くファイル名  
`Path(path_text).suffix`  .txt 拡張子(.が付く)  
`Path(path_text).parts`   ('c:', 'hoge', 'hoge2', 'hoge3.txt')  パスの各パーツを分離  

### 注意
- ファイル名を弄る場合(文字列計算をする場合)はカッコでくくること。
`new_filename = Path(path_text).parent / (Path(path_text).stem+"_new"+Path(path_text).suffix)`



