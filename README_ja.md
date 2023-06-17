# yakinori
日本語の漢字を平仮名/カタカナ/ローマ字に変換するライブラリです。  

mecab-unidic-NEologdに準じた日本語の文章の読みと発音を取得することができます。

ブログ記事: https://tech.morikatron.ai/entry/yakinori_kanji2kana_latin

## テスト環境
```
Ubuntu18.04
python==3.8.16
```

## インストール
２つの選択肢があります。
- Mecabとmecab-unidic-NEologdを環境に合わせてインストールする場合
- Dockerを使う場合


### 環境に合わせてインストールする場合
#### Ubuntuの場合
##### Mecabのインストール
```bash
$ sudo apt update
$ sudo apt install mecab libmecab-dev mecab-ipadic-utf8
```

##### mecab-unidic-NEologdのインストール
```bash
$ git clone --depth 1 https://github.com/neologd/mecab-unidic-neologd.git
$ cd mecab-unidic-neologd
$ sudo ./bin/install-mecab-unidic-neologd -n -y

# mecab-unidic-NEologdのインストールされたpathの表示
$ echo `mecab-config --dicdir`"/mecab-unidic-neologd"
> /usr/local/lib/mecab/dic/mecab-unidic-neologd

# mecab-unidic-NEologdをMecabのデフォルト辞書にしたい時
$ echo "dicdir = `mecab-config --dicdir`/mecab-unidic-neologd" | sudo tee /etc/mecabrc
$ sudo cp /etc/mecabrc /usr/local/etc

```

##### yakinoriのインストール
```bash
$ pip install yakinori
```

##### 最新のmecab-unidic-NEologdに更新したい場合
```bash
$ sudo ./bin/install-mecab-unidic-neologd -n -y
$ echo "dicdir = `mecab-config --dicdir`/mecab-unidic-neologd" | sudo tee /etc/mecabrc
$ sudo cp /etc/mecabrc /usr/local/etc
```

#### Dockerを使う場合
```bash
$ docker pull morikayamada/yakinori
```

## 使い方
### インポート
```python
>>> from yakinori import Yakinori
```

### インスタンスの作成
#### 環境に合わせてインストールした場合
- mecab-unidic-NEologdをMecabのデフォルト辞書にした場合はdic_pathを追加する必要はありません
```python
>>> yakinori = Yakinori()
```
- mecab-unidic-NEologdをMecabのデフォルト辞書にしていない場合はdic_pathを追加してください
```python
>>> yakinori = Yakinori(dic_path='path/to/mecab-unidic-NEologd') 
```
#### Dockerを使っている場合
Dockerの場合はdic_pathを追加する必要はありません
```python
>>> yakinori = Yakinori()
```

### 文を形態素解析する
```python
>>> sentence = "幽☆遊☆白書は最高の漫画です"
>>> parsed_list = yakinori.get_parsed_list(sentence)
```

### 読みを取得する
```python
# 平仮名に変換
>>> hiragana_sentence = yakinori.get_hiragana_sentence(parsed_list)
>>> print(hiragana_sentence)
ゆうゆうはくしょはさいこうのまんがです

# カタカナに変換
>>> katakana_sentence = yakinori.get_katakana_sentence(parsed_list)
>>> print(katakana_sentence)
ユウユウハクショハサイコウノマンガデス

# ローマ字に変換
>>> roma_sentence = yakinori.get_roma_sentence(parsed_list)
>>> print(roma_sentence)
yuuyuuhakushohasaikounomangadesu
```

### 発音を取得する
```python
# 平仮名に変換
>>> hiragana_sentence = yakinori.get_hiragana_sentence(parsed_list, is_hatsuon=True)
>>> print(hiragana_sentence)
ゆーゆーはくしょわさいこーのまんがです

# カタカナに変換
>>> katakana_sentence = yakinori.get_katakana_sentence(parsed_list, is_hatsuon=True)
>>> print(katakana_sentence)
ユーユーハクショワサイコーノマンガデス

# ローマ字に変換
>>> roma_sentence = yakinori.get_roma_sentence(parsed_list, is_hatsuon=True)
>>> print(roma_sentence)
yuｰyuｰhakushowasaikoｰnomangadesu
```

