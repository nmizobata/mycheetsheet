# class Getter/Setterについて
## Getter/Setterとは
- Classのプロパティ(変数)に対し、メソッドを超えて参照したり、外部からアクセスしたい場合は、クラス変数とするかself付インスタンス変数としてアクセス可能である。
  - 入力: class名.Property = a、self.Property = a
  - 参照: a = class名.Property, a = self.Property
- Getter/Setterは、この入力と参照をメソッドを使ってアクセスすることにあえて制限する概念である。
  - 入力: class setterProperty(self, a):
             self.Property = a
  - 参照: class getterProperty(self):
             return self.Property

## Getter/Setterを利用すべき理由
- プロパティによっては、値の型や、値の範囲を制限しないと、バグが発生する場合がある。
  - 特にPythonでは型宣言なく変数が使用できるため、値入力時にチェック機構が働かず、バグ発生の起因となりかねない。
  - また、本来参照すべきではない値を参照して外部でコーディングされてしまう懸念があり、その値の使われ方を変更するような改変を行った場合にバグ発生の起因となる。
- そこで、今後広範囲で利用される可能性が高いモジュールは、外部からアクセスできる変数の制限、および入力された場合のチェック機構を備えるGetter/Setterを使用するのが望ましい。
  - セッターでは、編集のチェックを行い、想定外の変数が入力された場合にはraise Exceptionを発生させる。
  - クラス内変数はすべてプライベート変数(__変数)とし、外部参照可とする変数のみ、ゲッターで参照させる。ゲッターには外部に出す型を統一するなど標準化を行う。

## Getter/Setterの問題点
- メソッドをつかって変数を入力/参照する場合、変数 = a という形で利用できず、使い勝手が悪いうえ、可読性が低くなる。
- pythonでは、getter/setterのデコレータが準備されており、このデコレータを使って、普通の値の入力参照のように使用することができるようになる。

## Getter/Setter関数の書き方
- メソッドはdef 変数名()で宣言する。メソッド名は変数のため同じ名前を使用することになる。
```
# getterの書き方
@property
def 変数名(self):
    return self.変数名

# setterの書き方
@変数名.setter
def 変数名(self, value):
    self.変数名 = value
```
```
class A
    def __init__(self):
        self.__name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

a = A.name
A.name = b
```

## 注意: Pythonのクラス変数
- Pythonではクラス変数を事前にクラス内で宣言しなくても外部から直接追加(動的追加)することができる。この柔軟性により、クラスで使用を想定していない変数を外部で入力後参照してもエラーにはならない。しかし、変数が衝突したり型エラーが起きたりするなどのリスクが高まることに注意が必要である。
```
class A:
    def __init__(self):
        pass

# クラス定義の外でクラス変数を追加
A.aaaa = "test"
b = A.aaaa
print(b)  # "test"と表示される
```
- クラス変数の動的な追加を禁止する方法の一つは__slots__の使用。__slots__=[]とすればすべてのクラス変数の動的追加を禁止することができる。(とはいえ、VSCodeではエラーが起きずに実行できているが)
```
class A:
    __slots__ = ['existing_var']

    def __init__(self):
        self.existing_var = "initial value"

# クラス定義の外でクラス変数を追加しようとするとエラーが発生する
A.aaaa = "test"  # AttributeError: 'A' object has no attribute 'aaaa'
```
