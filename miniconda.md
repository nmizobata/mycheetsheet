# Python/miniconda 環境構築
## condaでの仮想環境運用
- `conda create -n <仮想環境名>`  新規作成
- `activate 仮想環境名`  有効化
- `deactivate`          無効化: 
- `conda info -e`       仮想環境のリスト: 
- `conda list`          導入済のパッケージのリスト: 
- `conda env export >環境情報ファイル名.yml`   仮想環境情報の保存
- `conda env create -n <仮想環境名> -f 環境情報ファイル.yml`   仮想環境の複製
- `conda remove -n <仮想環境名>`               仮想環境の削除: 

## パッケージの追加
### 注
- 仮想環境を有効化したうえで必要なパッケージのみを追加すること。
-  「すべてのユーザーでインストール」とした場合は、Anaconda Prompt(miniconda3)を管理者権限で実行すること。
### Jupyter Notebook
- conda install jupyter (めちゃ時間がかかる)
- conda install jupyterlab-language-pack-ja-JP (jupyter7のメニューを日本語化)
- conda install jupytext (コードをpy形式でテキスト保存)
- conda install nbclassic (jupyter7インストール時の旧バージョンUI)
- conda install ipywidgets (ウィジェット機能)
- jupyter 拡張機能アドオン
	- pip3 install jupyter_contrib_nbextensions(jupyter7 Table of Contents等をおさめたアドオン群をインストールする)
	- jupyter contrib nbextension install --user
	- pip3 install jupyter_nbextensions_configurator(Jupyter 7のアドオン管理用のライブラリをインストールする)
	- jupyter nbextensions_configurator enable --user
		参考 nbextensionsがエラーになるとき
### 開発環境
- conda install black (自動整形)
- conda install ruff (記述ルールチェック)
- conda install pytest (テスト環境)
- conda install icecream  (デバッグ用ライブラリ)
### データサイエンス
- conda install sweetviz (機械学習分析用ライブラリ)
- conda install pandas_profiling (pandas DataFrameのサマリー表示)
- conda install matplotlib-fontja matplotlibの日本語化
- conda install pandas (numpy が同時にインストールされる)
- conda install seaborn (matplotlib が同時にインストールされる)
- conda install bokeh 
- pip3 install pandas_bokeh
- conda install plotly
### 機械学習
- conda install scikit-learn (機械学習)
### オフィス文書連携
- conda install openpyxl (pandas でread̲excel/to̲excel ができるように)
- conda install python-pptx (PowerPoint自動操作)
- pip3 install camelot-py (PDFスクレイピング)
	- pip3 install opencv-python (camelot-pyをインストールする場合はこれもインストールしておく必要あり)
	- pip3 install matplotlib (camelot-pyでPDFのレイアウトを表示する斎に使用する'
### Webスクレイピング
- conda install requests (Webスクレイピング)
- conda install beautifulsoup4 (Webスクレイピング)
- conda install lxml (beautifulsopu4用lxmlライブラリ)
- conda install selenium (Webスクレイピング)
- conda install scrapy (Webスクレイピング)
- selenium 4.6以降は不要(conda install webdriver-manager (Webスクレイピング, 最新webdriverをチェックしてインストール)
- conda install html5lib (HTML形式の表をpandasに読み込む)
- pip3 install requests-html (Webスクレイピング) あまりうまく動かない。
### 画像処理
- conda install pillow (画像処理ライブラリ)
### Google連携
- conda install google-api-python-client (Google認証)
- conda install google-auth-httplib2 (Google認証)
- conda install google-auth-oauthlib (Google認証)
### その他
- pip3 install slackweb (slackへのメッセージ送信)
- conda install schedule (定期処理)
- pip3 install jpholiday (日本の祝日)
- conda install mplfinance (株式表示)
- conda install ta-lib (株式分析)
- pip3 install pyti (株式分析)
- pip3 install pandas_datareader (株価取得)
- pip3 install investpy (投資情報サイトから情報取得)

## jupyter notebookの設定
### Jupyter Notebookの起動
- Anaconda Prompt(Miniconda3)を起動。
- コマンドラインで"jupyter-notebook"と打てば、起動する。
### Jupyter Notebook初期ディレクトリの変更・ブラウザの変更
参考記事: https://qiita.com/skytomo221/items/8f07734a63a3e7c15860
- Anaconda Prompt
```
jupyter notebook --generate-config
```
- C:\Users\username.jupyter\jupyter_notebook_config.pyを秀丸で編集。UTF-8で保存。
```
c.NotebookApp.browser = 'chrome'  # Notebookを使用するブラウザ
```
## matplotlib/seaborn
### 日本語化
IPAexGothicフォントの入手と各種設定ファイルの変更、およびmatplotlibキャッシュフォルダの削除。
参考記事: matplotlibの日本語化(フォント変更)
参考記事:【Seaborn】日本語を表示する (フォントを変更する)
1. matplotlibパッケージ保存先を知る  
jupyter notebookを起動して次を実行し保存先を得る
   ```
   import matplotlib.pyplot as plt
   plt.rcParams['datapth']
   plt.matplotlib_fname()
   ```
1. IPAexGothicフォントをfonts/ttfに格納
   1. IPAexGothicフォント(ipaexg00401.zip(4.0MB))の入手
   2. 解凍して得た*.ttfを..../site-packages/matplotlib/mpl-data/fonts/ttf/にコピー。
1. matplotlibrcを編集(matplotlibの設定ファイル)
   1. ..../matplotlib/mpl-data/matplotlibrcをエディタで開く
   2. font.familyを変更
   ```
   # font.family : sans-serif ← これを残しておくとwarningが出るので消す
   font.family   : IPAexGothic
   ```
1. rcmod.pyを編集(Seabornの設定ファイル)
   1. ..../site-packages/seaborn/rcmod.pyをエディタで開く
   2. sans-serifをIPAexGothicに変更。(2カ所)
   ```
   #def set(context="notebook", style="darkgrid", palette="deep", font="sans-serif", font_scale=1, rc=None): 
   def set(context="notebook", style="darkgrid", palette="deep", font="IPAexGothic", font_scale=1, rc=None):
   ```
   ```
   #"font.family": ["sans-serif"] 
   "font.family": ["IPAexGothic"],
   ```
1. matplotlibのキャッシュフォルダを削除
   - C:/Users/blues/.matplotlibをフォルダごと削除しフォントキャッシュをクリアにする
   - jupyter notebookを起動し、デフォルトのフォントファミリーを確認する
   ```
   import matplotlib.pyplot as plt 
   print(plt.rcParams['font.family'])
   ```
## Seleniumの設定(Bokehのexport_pngでも利用)
- 現在使用のChromeのバージョンにあったChrome Driverを入手しPathの通ったフォルダに格納する。
- 参考記事: Python + Selenium で Chrome の自動操作を一通り
## Chromeバージョンを確認しChromeドライバを入手
- Chrome>ヘルプ>Chromeについてからバージョンを確認。
- バージョンにあったChromeドライバをダウンロード
- 現在有効なPATHを確認しChromeドライバーを格納
- PCアイコンのプロバティ>システムの詳細設定>環境変数>ユーザー環境変数のPathを編集で内容確認
- PATHが通っているフォルダ(miniconda/Scriptsなど)にChromeドライバを格納。
## python *.pyのためのpath設定
コマンドプロンプトを起動しpythonのバージョンを確認するコマンドを実行
```
python --version
```
- 単に｢python｣が表示される場合、ダミーが起動しているだけでpythonの実行はできない。
  ダミー設定を消す。Windowsの設定>アプリ>アプリ実行エイリアス>アプリインストーラ python.exe、python3.exeをオフにする。
- pythonをインストールしているはずなのに｢内部コマンドまたは外部コマンド、操作可能なプログラムまたはバッチファイルとして認識されていません」が表示される場合、PATHが通っていないのでPATHの設定をする。
	- minicondaのpython.exeの場所を確認。(.../miniconda3/python.exe)
	- PCアイコンのプロバティ>システムの詳細設定>環境変数>ユーザー環境変数のPathを編集。(検索窓で「path」と入力し「システム環境変数の変数>環境変数...＞Pathで編集」)
	  
	  自分用にインストールした場合: %USERPROFILE%\miniconda3
	  
	  すべてのユーザーでminicondaをインストールした場合: c:\ProgramData\miniconda3
- バージョンが表示されれば問題無し。

## Anacondaの削除
1. anaconda-clean を実行する
   - anaconda-cleanでanacondaやPythonライブラリが作ったデータファイルを削除。
   ```
   $ conda install anaconda-clean
   $ anaconda-clean
   $ rm -fr ~/.anaconda_backup
   ```

1. プログラムの削除からanacondaをアンインストールする
1. [MiniCondaのインストール](https://docs.conda.io/en/latest/miniconda.html)  
1. condaのチャネルをconda-forgeに固定
   - スタートメニューから、Anaconda Prompt(Miniconda3)を起動。
   - conda config --show channels でどのチャネルが設定されているかが分かる。
   - conda config --remove channels defaults でdefault チャネル削除。
   - conda config --add channels conda-forge でconda-forge チャネルを追加。
