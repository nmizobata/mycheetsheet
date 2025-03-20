# Python typing(型ヒント)のメモ
## 宣言
- `import typing`または`from typing import List, Dict`のように宣言する。
- `import typing`の場合は、`typing.List[str]`のように使用する。
## ListやDictのような複数の変数からなる型
### 使用方法
- typing.List[str]
- typing.Dict[str,str]
- typing.Set[str]
- typing.
### 空のList、Dictが使われる場合
- 空のList、Dictが使われる場合でも、上記宣言でエラーにならない。
- ただし、Noneが使われる場合は後述のとおりOptionalを使用する。
## 複数の型が使用される場合
- int型とstr型が使用される場合は、`str|int`のように'|'を挟んで列記する
## 通常の型に加えてNoneも使われる可能性がある場合
- Optionalを使用する。
  - 例 NoneとDict型が使われる場合。`typing.Optional[typing.Dict[str,str]]`
- `|`を使用する。
- - 例 NoneとDict型が使われる場合。`typing.Dict[str,str] | None`
## class宣言の前に型ヒントを使いたい場合
- 同じコードファイルの中で、後方で定義されているクラスを、先に型ヒントに使うと「定義されていない」エラーが起きる。
- この場合は、以下の宣言をファイルのトップで行う。(コメント文よりも先に宣言しないとエラーになる)
  ```
  from __future__ import annotations
  ```
## Pandas
```
import pandas as pd

def test()-> pd.DataFrame
def test2()-> pd.Series
```
等。
