<div align="right">
  <a href="README.md">English</a> | <a>日本語</a>
</div>

<div align="center">
  <a href="https://github.com/tcu-masuda-lab/test">
    <img alt="deepmaldetect" src="./resources/logo.png" width="300">
  </a>
</div>

<h2 align="center">
  DeepMalDetect - DNN-Based Malware Detection.
</h2>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&style=for-the-badge&logo=pytorch&logoColor=white)

このリポジトリでは下記の論文で示す実験内で作成したモデルを公開しています。モデルの作成には[elastic/ember](https://github.com/elastic/ember)で公開されている`ember_dataset_2018`を使用しています。このDNNを用いたマルウェア検出モデルはハイパーパラメーターチューニングを通じて精度を向上させています。

モデルや実験に関する詳細はこちらの論文をご覧ください：
<br>
***Parallel-processed Hyperparameter Tuning for Higher Accuracy of Malware Detection***
<br>
https://doi.org/10.1145/3731763.3731797

## ライセンス
このプロジェクトには、GNU Affero General Public License バージョン 3 (AGPL‑v3) のもとでライセンスされた[elastic/ember](https://github.com/elastic/ember)リポジトリのコードが一部含まれています。AGPL‑v3 のライセンス条件については、LICENSE ファイルを参照してください。

また、モデルの学習には、MIT ライセンスのもとで提供されている```ember_dataset_2018```データセットを使用しています。

## 特徴
このリポジトリを使用すると、精度の高いDNNベースのマルウェア検出モデルを使用した実験を再現できます。精度の高さは正解率や再現率を用いて評価されており、[先行研究](https://www.mecs-press.org/ijcnis/ijcnis-v14-n2/IJCNIS-V14-N2-2.pdf)で示すモデルと同一のエポック数でありながら高い性能を示しています。

研究者は本リポジトリで公開されているモデルを研究の比較対象として用いることが出来ます。

## インストール方法

### 実行環境
モデル作成時のPython 3.9.13での実行を想定しています。<br>
推奨環境はPython 3.9系です。

### gitからインストールする

```
git clone https://github.com/tcu-masuda-lab/test.git
```

### リポジトリをクローンしたら仮想環境を作成する

```
python3 -m venv .venv
```

### 仮想環境を有効化するためのポリシーを設定する

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 仮想環境を有効化

```
.venv\Scripts\activate
```

### pipをアップデート

```
python.exe -m pip install --upgrade pip
```

### 必要なライブラリをインストール

```
pip install -r requirements.txt
```

## 使用方法
```predict```は任意のPE ファイルに対して予測を行うことができます。この関数は0~1の値を出力するため、0.5と比較することで、マルウェアか否か(True or False)の判断することが出来ます。
```python
import deepmaldetect as dmd
dest = "sample.exe"
raw_data = open(dest, "rb").read()
pred = dmd.predict(raw_data) > 0.5
print(f"{dest}: {pred}")
```

## 引用について
このモデルを出版物で使用する場合は下記の[論文](https://dl.acm.org/doi/full/10.1145/3731763.3731797)を引用してください:
```
@inproceedings{10.1145/3731763.3731797,
  author = {Sangawa, Gakuto and Masuda, Satoshi},
  title = {Parallel-processed Hyperparameter Tuning for Higher Accuracy of Malware Detection},
  year = {2025},
  isbn = {9798400710841},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3731763.3731797},
  doi = {10.1145/3731763.3731797},
  booktitle = {Proceedings of the 2025 10th International Conference on Intelligent Information Technology},
  pages = {130–135},
  numpages = {6},
  keywords = {malware detection, machine learning, static analysis},
  location = {
  },
  series = {ICIIT '25}
}
```