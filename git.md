要確認
- Githubには新しいコミットがあり、ローカルのプロジェクトでGithubをプルする前にdevelopmentブランチで編集作業を開始。
- developブランチでファイルを編集保存した後、masterにチェックアウト。この状況では、Github上の新しいコミットは未反映にも関わらず、masterにさきほど編集したファイルが生成された状況。
- ここでgit pull origin masterでgithubからマスターにプルしようとしても、すでにアップデート済と言われる。(一部のファイルはGithubの方が新しいにもかかわらず、である)
- githubとの同期をとるブランチ(ここではmaster)と、ローカルで編集するブランチ(ここではdevelopment)は必ず分けること。
- 編集ブランチでファイルを編集し保存しても、masterに移動しなければ、git pull origin masterの実行は可能。(masterブランチはGithubの最新の構成、developmentブランチは先ほど編集したファイル以外はmasterブランチよりと同等または古いファイル)となる。
- 編集ブランチでgit mergeを実行し、github/masterと同期を取る。この際、競合する場合は競合を解消する。


## Gitコマンド
### Git初期設定
- git config --global user.name mizobata
- git config --global user.email bluesky@mizobata.com
- git config --global core.editor "code --wait": 主エディタをvscodeにする
- git config --global http.proxy http://proxy.fujixerox.com:8080
- git config --global init.defaultBranch master
- git config --list
- git init: ローカルレポジトリを作る
### ブランチ操作
- git branch ブランチ名： ブランチの作成
- git checkout ブランチ名： 操作対象をブランチに移行。git switch ブランチ名でも同じ。
- git checkout -b ブランチ名： 「git branch ブランチ名」 + 「git checkout ブランチ名」
- git branch : 現在のブランチリストを表示 (現在のブランチには＊がついている) 
- git branch -d [ブランチ名]: ブランチの削除(マージ済)
- git branch -D [ブランチ名]：ブランチの強制削除(未マージのものも含む)
### コミット
- git add . : すべてのファイルのステージング
- git add -f フォルダ : (新規追加等で)アントラックになっているフォルダを追加
- git commit : ステージングしたファイルのコミット
- git commit -a : アントラックファイルを除いた変更ファイルをステージング&コミット
- git commit -m "メッセージ" : コミットコメントを付加してコミット
### リストア
- git checkout -- . : ワークエリアのファイルを直前の状態(ステージングエリアのファイルの状態)に戻す (git restore .)
- git reset HEAD . : ステージングエリアのファイルを、最終コミットの状態に戻す
### リポジトリからの削除
- git rm aaa.txt : aaa.txtのファイル削除と同時にgit管理からも外す
- git rm -r directory : directoryとそれ以下のファイルを削除すると同時にgit管理からも外す
### 情報確認
- git status: ワーキングエリアの状態を確認
- git log : コミット履歴  git log -p 差分情報も表示
- git log master origin/master: ローカルとリモートのコミットの状況比較
- git ls-files: gitで管理しているファイルのリスト
- git status -ignored: gitの管理から外されているファイルのリスト
### 差分確認
- git diff : ワーキングエリアとステージングエリアのファイルの差分を表示
- git diff --cached : ステージングエリアと最終コミットとの差分を表示
- git diff master : (ブランチにいるとき)master(最終コミット)との差分を確認
### リモートリポジトリ操作
- git remote add origin https:\\(githubリポジトリURL) : gitにhubリポジトリをリンクする
- git remote set-url origin (変更後のリポジトリURL) : 新しいgithubリポジトリのURLをoriginに割り当てる
- git push origin ローカルブランチ名： github(origin)に指定したローカルブランチをアップする(どこのブランチにいても他のブランチを指定できる)
  ローカルとリモートのブランチ名が異なる場合は： git push origin ローカルブランチ名:リモートブランチ名
- git push -u origin master: ローカルのmasterブランチで今後pushする場合はgit pushで済ませられるようになる。(-uオプション: origin/masterを「上流ブランチ」設定。上流ブランチは、各ブランチごとに設定する)
- git branch -vv: 上流ブランチの確認

# Git学習メモ
参考 [サル先生のGit入門](https://backlog.com/ja/git-tutorial/)

## 作業の流れ
#### ローカルPC上の作業で閉じる場合
1. git初期化および初期状態の保存(@master)： git init > git add . > git commit
2. ブランチを作成して編集(@ブランチ) : git branch ブランチ名 > 作業 > git add . > git commit
3. masterをマージ(@ブランチ) : git merge master  複数のブランチで並行作業している場合masterが開始時点と異なっている場合があるため。
4. コンフリクトが起きたら解決し、コミット(@ブランチ) ： 編集 > git add . > git commit
5. masterに移動しブランチの最終コミットをマージ: git checkout master > git merge ブランチ名
#### GitHubで共同作業する場合その1(自分がプロジェクトを開始する場合)
1. git初期化および初期状態の保存(@master)： git init > git add . > git commit
3. ローカルとGitHubをリンク: git remote add origin GitHubリポジトリのURL
4. GitHubの中身を確認しGitHubへ投稿: git remote -v > git push origin master
5. ブランチを作成して編集(@ブランチ): git branch ブランチ名 > 作業 > git add . > git commit
6. GitHubにブランチをPushしプルリクエストを作成(@GitHub)： git push origin ブランチ名 > GitHubでプルリクエストを作成
7. GitHub上でコンフリクトが発生しているかを確認(@GitHub)
8. コンフリクトが発生した場合、A. GitHub上で修正しコンフリクトマークを解除 または B. ローカルのmasterをアップデートしてブランチ上でコンフリクトを解消する
8B-1. masterブランチに移動しGitHubのMasterをプル(@master)： git checkout master > git pull orgin master
8B-2. 編集ブランチに移動しマージ、コンフリクト発生させる(@ブランチ): git checkout ブランチ名 > git merge master
8B-3. vscodeでコンフリクトを解決し、コミット(@ブランチ): 編集 > git add . > git commit
8B-4. GitHubへPushしプルリクエストを作成(@GitHub): git push origin ブランチ名 > GitHubでプルリクエストを作成
8B-5. GitHub上でコンフリクトが発生しているかを確認(@GitHub)
8B-6..GitHub上でマージの問題なければマージ実行
9. masterに移動しGitHubからプルしコミット: git pull origin master > git add . > git commit
10. ブランチに移動しmasterとマージしてコミット: git merge master
#### GitHubで共同作業する場合その2(すでにGitHubで存在するプロジェクトに参加する場合)
1. GitHubからクローン作製: git clone GitHubリポジトリのURL
2. プロジェクトフォルダに入りGitHub名を定義: git remote add origin GitHubリポジトリのURL
これ以降はGitHubで共同作業する場合その1の5以降と同じ。
#### 他者のGithubリポジトリをコピー取得
1. 他者のリモートリポジトリを開き、右上のForkで自分のGithubアカウントにリポジトリをコピーする。
2. 自分のGithubアカウントにコピーしたリポジトリをローカルリポジトリにクローンする。 git clone GitHubリポジトリのURL
3. プロジェクトフォルダに入りGitHub名を定義: git remote add origin GitHubリポジトリのURL
これ以降はGitHubで共同作業する場合その1の5以降と同じ。

## git bash
### 設定
- 日本語文字化けの場合Options > Text > Font(Terminal,10pt), Locale(ja_JP), Character set(UTF-8)
- 設定が終わったらgit bashを再起動
- 上記でgit ls-filesで文字化けする場合は、git bashで
```
$ git config --local core.quotepath false
$ git config --global core.quotepath false
```
### ビューワー操作
- q: end
- j or e: 1行上
- k or y: 1行下
- f: 1ページ進む
- b: 1ページ戻る

## 戻したいときのコマンド
[参考1](https://qiita.com/rch1223/items/9377446c3d010d91399b) [参考2](https://git-scm.com/book/ja/v2/Git-のさまざまなツール-リセットコマンド詳説#_チェックアウトとの違い)

### コミット取り消し
- git logで戻したいコミットのハッシュ値を確認。ハッシュ値はマウスでコピペするか、頭4ケタを指定する。
#### ステージングに戻す
- コミット自体をなかったものにする: git reset --soft [戻り先のハッシュ番号]
#### 未ステージングに戻す
- コミット自体をなかったものにする: git reset [戻り先のハッシュ番号] / git reset --mixed [戻り先のハッシュ番号]
- コミット中止のコミットを新規作成: git revert [取り消しコミットのハッシュ番号]
  (コミット中止のコミットも中止できる)
#### 編集も取り消し (直前コミット状態に戻す)
- コミット自体をなかったものにする: git reset --hard [直前コミットハッシュ番号]
### ステージング取り消し
#### 単純に未ステージングに戻す(編集は残す)
- 特定ファイル: git reset [ファイル名] または git restore --staged [ファイル名]
- すべて: git reset / git reset --mixed または git restore --staged .
#### 編集も取り消し (直前コミット状態に戻す)
- 特定ファイル: git reset --hard ファイル名 / git checkout ファイル名
- すべて: git reset --hard / git checkout .
### 編集取り消し (任意のコミット状態に戻す)
- 特定ファイルのみ: git checkout [コミットid] [ファイルパス]
- すべてのファイル: git reset --hard [戻り先のハッシュ番号] 
### 削除したブランチの復活 (指定コミット状態を指定したブランチに再生)
- git reflogでHEAD@{番号} > git branch [新ブランチ] HEAD@{番号}。 [新ブランチ]が作成され復活。なおHEAD@{}はすぐに変わるのでreflogを確認したらすぐに実行すること。

## .gitignore
.gitignoreの記入例: https://github.com/github/gitignore
- ファイル、フォルダとも区別せずに名称を記述
- すでに管理対象になっているファイルは、.gitignoreへの登録だけでなく、管理対象から外す作業が必要。
  - git rm --cached aaa.txt : aaa.txtは残しつつgit管理からも外す
  - git rm -r --cached directory* : directoryとそれ以下のファイルを残しつつgit管理からも外す
* directryは、フォルダ名だけでなくGitのルートからのパスを記述する。

## Github SSH Keyの設定
### SSH keyの生成
> ssh-keygen -t ed25519 -C "bluesky@mizobata.com"
### 公開キーをクリップボードにコピー
> clip < /c/Users/mizobata/.ssh/id_ed25519.pub
Github設定画面に設定
Github Setting> SSH Key > SSH andGPG Keys > New SSH Keyをクリック。
### 公開キーを張り付ける
Title: (どのパソコンで発行したものかを入れておくとよい) 
Key: 公開キーをペースト
Add SSH keyを押す
### 設定の確認
> ssh -T git@github.com
パスフレーズを入力

## 現在の編集の一時退避～別作業実施～元の作業に戻る
現在の作業をいったん中止(変更部分はいったん削除)、別の作業を行ったうえで、元の作業に戻るときにはスタッシュ機能を使用する。
- git stash : 一時退避
- git stash list : 一時退避した内容のリスト
- git stash pop : 一時退避解除
一時退避中にブランチを作成/移動した場合は、編集中のブランチの移動と同じ動作になる。
退避した作業の変更部分と、退避中に行った変更部分とでコンフリクトが発生する場合は、通常のコンフリクトの対処と同じように対処する。
   
## VSCodeの起動
開いているフォルダで右クリック VSCodeを起動
開いているフォルダで実行されているGit Bashコマンドラインでcode .を実行
(参考: エクスプローラの起動 start .)

## ブランチの運用
- masterブランチは「安定したもの」「確定したもの」に限定すること。
- ブランチ名には日本語も使用できる。また"feature/picture"など記号も使用可能。
- 改変する場合は必ず作業用のブランチを新たに作って行い、作業が完了(動作が安定していることも確認)したらmasterにマージすること。
- 常にどのブランチに対して操作を行うのか、を意識する。操作対象のブランチは git checkout ブランチ名で指定する。
- ブランチを作らずに編集を始めてしまっても、ステージングエリアに登録する前なら、後付けてbranchを作成、移動することができる。
- 間違ってステージングしてしまっても、編集内容は保存されたままgit resetでステージングを解除可能。後付けでbranchを作成し、移動することができる。
- 元のファイルとの差分はgit diff masterで確認することができる。
- (コミットする前に)元のファイルに戻したい場合はgit restore . (git checkout -- .)で戻すことができる
- (コミットした後に)masterブランチの状態に戻したい場合は、masterに移動しブランチを削除したうえでまた新しくブランチを作成する？
- ブランチで作業中に、他のブランチのmasterへのマージが行われた場合は、作業中のブランチにmasterの最新状態を取り込んでおく。
## ブランチの統合(mergeとrebase)
### merge
- 作業ブランチを統合ブランチに取り込むときに行う。
- 統合ブランチ(以下master)が、作業ブランチ開始時点から変更されていない場合は、作業ブランチの先頭がmasterブランチの先頭となる。(fast-forwardマージと呼ぶ)
- 統合ブランチが、作業ブランチ開始時点から変更さあれている場合は、両方の変更を取り込んだマージコミットが新たに作成される。(masterブランチのコミットでも作業ブランチのコミットでもない新しいコミット)
### rebase
- 統合ブランチを作業ブランチに取り込むときに行う。
- 統合ブランチ(以下master)が、作業ブランチ開始時点から変更されていない場合は、mergeと同じ処理が行われる。
- 統合ブランチが、作業ブランチ開始時点から変更さあれている場合は、masterの最新履歴の後に作業ブランチが接続される形で一本化される。(競合が発生する場合は、修正を入れる) ＝ 作業ブランチの起点をmasterの最新コミットの位置にずらす動きをする。この状態は、merger fast-forwardが可能な状態であるので、さらにmergeを行う。

### 共同作業をしている場合
#### 考え方
- Githubの統合ブランチ(master や development)は自分の知らないところで「常に更新されている」との意識を持っておく
- 自分の作業を統合ラインに反映させるためには、自分のブランチをGithubへpushし、プルリクエストでマージを要求。承認されたらマージを実施する。
#### 手順
0. 自分の作業ブランチとmaster(=githubのmaster)との比較、差異を確認する。できれば、最新のmasterを作業ブランチの出発点に変更する、rebaseを行う。
   1. ローカルのmasterにリモートmasterをプルする。
      - git pull origin master
   2. 作業ブランチとmasterの差異を確認する。
      - git diff master
   3. fast-fowardマージが可能な場合は実施。そうでない場合はrebaseをできれば行ったほうが、後の作業が楽になる。
      - git stash -u (新規作成ファイルも含ませるために-uを使う)
      - git rebase master
      - 競合が起きた場合は修正
      - git add 修正ファイル
      - git rebase --continue

1. 自分の作業が終了したら、作業ブランチをコミット
2. リモートリポジトリへpush(リモートで同じ名前(or違う名前に指定も可)
	git push origin <ブランチ名>
3. ブラウザでリポジトリを開きpull request作成を行う。
  - どのブランチ(右側)から、どのブランチ(左側)にマージしたいのかを指定する。
  - 注意: フォークした場合は、フォーク元が右側に表示されているので、自分のリモートリポジトリにするように注意
  - コメントとレビュワーを指定。
  - レビュワーはコメントを入れて返す。LGTM (looks good to me)はよく使われる
  - コミュニケーションが終了したらブランチをmasterブランチにマージする。
    - マージ方法①Create a merge commit: すべてのコミット履歴を残してマージ
    - マージ方法②Squash and merge: ブランチの履歴を一つのコミットにまとめてマージ。
    - マージ方法③Rebase and merge: ブランチの起点をベースブランチの最新時点に切り替えてマージ。複数のブランチが一直線の履歴で表現できるようになる。
3. a. レビュワーが自分のローカルリポジトリにブランチを取り込んでみたい場合(自分のところでアプリケーションを実行するなど)、以下のように行えばgitはリモートからブランチを取り込んでくる。
  - git fetch originでフェッチだけを行う
  - git checkout <ブランチ>
4. リモートリポジトリでマージが行われたら、ローカルリポジトリへプル(＝フェッチ＋マージ)を行う。(自分が編集中であってもbranchで行っておりmasterにプルしても影響はないはず)
- masterブランチに切り替える。(ブランチを切り替えずにプルを行うと今のブランチにマスターブランチがマージされてしまうので注意)　
   git checkout master (ローカルのmasterブランチに移動するという意味。作業中のブランチがある場合はコミットしておく必要がある)
   git pull origin master  (originのmasterブランチを取り込む、という意味)
どうしても、リポジトリはともかく自分のワークツリーに反映したくないときはフェッチだけ行う。git fetch origin
5. ブランチで作業中に、他のブランチのmasterへのマージが完了したら、都度、作業中のブランチにもマージしておく。
   git checkout 作業ブランチ名  (ローカルの作業ブランチに移動)
   git pull origin master  (originのmasterブランチを取り込む)
   (マージコメントが求められるが、特に不要なのですぐに閉じてよい)

## オープンソフトウェアの世界
### 検索方法
- "/"で検索。https://help.github.com/articles/searching-for-repositories/を参照。
- stars :>= 10000 でStarが10000個以上のリポジトリ。
- starts:>=10000 language:pythonでpython言語の検索。
- ReadMEファイルにおけるMarkDownの記法。http://guides.github.com/features/mastering-markdown/

## Githubの機能
### default branch
main/masterブランチを隠蔽し他のメンバーがデフォルトとして使用するブランチを指定する。
setting > general > default branch
### issue
Todo管理。

