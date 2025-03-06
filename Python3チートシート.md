[Python3チートシート](https://qiita.com/1429takahiro/items/710a877b1afb1626334f#7-%E7%B5%84%E3%81%BF%E8%BE%BC%E3%81%BF%E9%96%A2%E6%95%B0%E7%89%B9%E6%AE%8A%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89)


## 既存クラスの機能拡張方法 (Co-pilotより)
### クラス(Chart)に対する機能拡張クラス(ChartBuilder)
`Chart`クラスをベースクラスとして継承した`ChartBuilder`クラスを用意し、独自の機能を追加する。これで`ChartBuilder`クラスを`Chart`クラスの機能を引き継ぎつつ、独自の処理を追加できる。

```python
class Chart:
    def __init__(self, title, x_label, y_label):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def show(self):
        print(f"Title: {self.title}, 
              X Label: {self.x_label}, Y Label: {self.y_label}")

class ChartBuilder(Chart):
    def __init__(self, title, x_label, y_label, 
                 folder_paths, transform_params):
        super().__init__(title, x_label, y_label)
        self.folder_paths = folder_paths
        self.transform_params = transform_params

    def build_chart(self):
        # フォルダパスや変換パラメータを使って具体的なチャートを構築する処理
        print(f"Building chart with folders: {self.folder_paths} 
                and transform parameters: {self.transform_params}")

# 使用例
chart_builder = ChartBuilder("Sample Chart", "X-Axis", "Y-Axis", 
                             ["path1", "path2"], {"param1": "value1"})
chart_builder.show()
chart_builder.build_chart()
```

この例では、`ChartBuilder`クラスが`Chart`クラスを継承し、共通の属性やメソッド（`title`, `x_label`, `y_label`, `show()`メソッド）を引き継いでいます。さらに、`ChartBuilder`クラスには`folder_paths`や`transform_params`といった追加の属性や、`build_chart()`という新しいメソッドが追加されています。

このように設計することで、`ChartBuilder`クラスは`Chart`クラスと同じように扱いつつ、独自の処理を追加することができます。

### 既存クラス(Chart)のインスタンスに対し機能拡張したい場合。コンポジションの例。
既存の`chart_obj`インスタンスに対して、`ChartBuilder`の機能を追加する方法としては、デコレーターやコンポジションの手法を使う。下はコンポジションの手法の例。

```python
class Chart:
    def __init__(self, title, x_label, y_label):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def show(self):
        print(f"Title: {self.title}, 
              X Label: {self.x_label}, Y Label: {self.y_label}")

class ChartBuilder:
    def __init__(self, chart, folder_paths, transform_params):
        self.chart = chart
        self.folder_paths = folder_paths
        self.transform_params = transform_params

    def build_chart(self):
        # フォルダパスや変換パラメータを使って具体的なチャートを構築する処理
        print(f"Building chart with folders: {self.folder_paths} 
                and transform parameters: {self.transform_params}")

    def __getattr__(self, attr):
        # Chartクラスのメソッドにアクセスできるようにする
        return getattr(self.chart, attr)

# 既存のChartインスタンス
chart_obj = Chart("Sample Chart", "X-Axis", "Y-Axis")

# ChartBuilderの機能を追加
chart_builder = ChartBuilder(chart_obj, 
                             ["path1", "path2"], {"param1": "value1"})

# Chartクラスのメソッドを呼び出す
chart_builder.show()

# ChartBuilder独自のメソッドを呼び出す
chart_builder.build_chart()
```

この例では、`ChartBuilder`クラスは`Chart`クラスのインスタンスを保持し、`__getattr__`メソッドをオーバーライドすることで、`Chart`クラスのメソッドにアクセスできるようにしています。これにより、`ChartBuilder`クラスを通じて`Chart`クラスの機能をそのまま利用しつつ、新たな機能を追加することができます。

### デコレーターの例
デコレーターを使って、既存の`Chart`クラスに追加機能を付与する方法は以下のように実装できます：

```python
class Chart:
    def __init__(self, title, x_label, y_label):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def show(self):
        print(f"Title: {self.title}, X Label: {self.x_label}, Y Label: {self.y_label}")

def chart_builder_decorator(func):
    def wrapper(chart, folder_paths, transform_params):
        chart.folder_paths = folder_paths
        chart.transform_params = transform_params
        func(chart)
    return wrapper

@chart_builder_decorator
def build_chart(chart):
    # フォルダパスや変換パラメータを使って具体的なチャートを構築する処理
    print(f"Building chart with folders: {chart.folder_paths} and transform parameters: {chart.transform_params}")

# 既存のChartインスタンス
chart_obj = Chart("Sample Chart", "X-Axis", "Y-Axis")

# ChartBuilderの機能を追加
build_chart(chart_obj, ["path1", "path2"], {"param1": "value1"})

# Chartクラスのメソッドを呼び出す
chart_obj.show()
```

この例では、`chart_builder_decorator`デコレーターを定義し、`build_chart`関数に適用しています。デコレーター内部で、`Chart`インスタンスに対して`folder_paths`と`transform_params`属性を追加し、元の関数を呼び出します。

これにより、既存の`Chart`クラスに対して追加機能を付与しつつ、既存のメソッドもそのまま利用することができます。
