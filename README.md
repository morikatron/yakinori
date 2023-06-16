# yakinori
Japanese Converter Kanji to Hiragana, Katakana, Latin alphabet.  
日本語の漢字を平仮名/カタカナ/ローマ字に変換するライブラリです。  

You can get the reading and pronunciation of Japanese sentences based on mecab-unidic-NEologd.  
mecab-unidic-NEologdに準じた日本語の文章の読みと発音を取得することができます。

ブログ記事: TODO:公開されたブログ記事のURLを貼る

## Test Environments（テスト環境）
```
Ubuntu18.04
python==3.8.16
```

## Install
There are two options to install.（２つの選択肢があります。）
- Install Mecab and mecab-unidic-NEologd in your own environment  
（Mecabとmecab-unidic-NEologdを環境に合わせてインストールする場合）
- Use Docker（Dockerを使う場合）


### Your Own Environment（環境に合わせてインストールする場合）
#### For Ubuntu（Ubuntuの場合）
##### Install Mecab（Mecabのインストール）
```
$ sudo apt update
$ sudo apt install mecab libmecab-dev mecab-ipadic-utf8
```

##### Install mecab-unidic-NEologd（mecab-unidic-NEologdのインストール）
```
$ git clone --depth 1 https://github.com/neologd/mecab-unidic-neologd.git
$ cd mecab-unidic-neologd
$ sudo ./bin/install-mecab-unidic-neologd -n -y

# show installed mecab-unidic-NEologd dictionary path（mecab-unidic-NEologdのインストールされたpathの表示）
$ echo `mecab-config --dicdir`"/mecab-unidic-neologd"
> /usr/local/lib/mecab/dic/mecab-unidic-neologd

# If you want to make mecab-unidic-NEologd as defalut dictionary, run commands below.（mecab-unidic-NEologdをMecabのデフォルト辞書にしたい時）
$ echo "dicdir = `mecab-config --dicdir`/mecab-unidic-neologd" | sudo tee /etc/mecabrc
$ sudo cp /etc/mecabrc /usr/local/etc

```

##### Install yakinori（yakinoriのインストール）
```
$ pip install git+ssh://git@github.com/morikatron/yakinori.git
# $ pip install yakinori # TODO:PyPIで公開したらこちらにする
```

##### You can update the recent mecab-unidic-NEologd（最新のmecab-unidic-NEologdに更新したい場合）
```
$ sudo ./bin/install-mecab-unidic-neologd -n -y
$ echo "dicdir = `mecab-config --dicdir`/mecab-unidic-neologd" | sudo tee /etc/mecabrc
$ sudo cp /etc/mecabrc /usr/local/etc
```

#### Use Docker（Dockerを使う場合）
```
$ docker image build --network host -t yakinori .
$ docker run -it --name yakinori yakinori /bin/bash
# TODO: docker hubで公開したらこちらにする
```

## How to use（使い方）
### Import（インポート）
```python
>>> from yakinori import Yakinori
```

### create Instance（インスタンスの作成）
#### Installed on your Own Environment（環境に合わせてインストールした場合）
- If you made mecab-unidic-NEologd as defalut dictionary, you don't need to add dic_path.  
（mecab-unidic-NEologdをMecabのデフォルト辞書にした場合はdic_pathを追加する必要はありません）
```python
>>> yakinori = Yakinori()
```
- If you did not make mecab-unidic-NEologd as defalut dictionary, add dic_path.  
（mecab-unidic-NEologdをMecabのデフォルト辞書にしていない場合はdic_pathを追加してください）
```python
>>> yakinori = Yakinori(dic_path='path/to/mecab-unidic-NEologd') 
```
#### Using Docker（Dockerを使っている場合）
If you use Docker, you don't need to add dic_path.  
（Dockerの場合はdic_pathを追加する必要はありません）
```python
>>> yakinori = Yakinori()
```

### Parse Sentence（文を形態素解析する）
```python
>>> sentence = "幽☆遊☆白書は最高の漫画です"
>>> parsed_list = yakinori.get_parsed_list(sentence)
```

### Get Reading（読みを取得する）
```python
# convert to hiragana（平仮名に変換）
>>> hiragana_sentence = yakinori.get_hiragana_sentence(parsed_list)
>>> print(hiragana_sentence)
ゆうゆうはくしょはさいこうのまんがです

# convert to katakana（カタカナに変換）
>>> katakana_sentence = yakinori.get_katakana_sentence(parsed_list)
>>> print(katakana_sentence)
ユウユウハクショハサイコウノマンガデス

# convert to Latin alphabet（ローマ字に変換）
>>> roma_sentence = yakinori.get_roma_sentence(parsed_list)
>>> print(roma_sentence)
yuuyuuhakushohasaikounomangadesu
```

### Get Pronunciation（発音を取得する）
```python
# convert to hiragana（平仮名に変換）
>>> hiragana_sentence = yakinori.get_hiragana_sentence(parsed_list, is_hatsuon=True)
>>> print(hiragana_sentence)
ゆーゆーはくしょわさいこーのまんがです

# convert to katakana（カタカナに変換）
>>> katakana_sentence = yakinori.get_katakana_sentence(parsed_list, is_hatsuon=True)
>>> print(katakana_sentence)
ユーユーハクショワサイコーノマンガデス

# convert to Latin alphabet（ローマ字に変換）
>>> roma_sentence = yakinori.get_roma_sentence(parsed_list, is_hatsuon=True)
>>> print(roma_sentence)
yuｰyuｰhakushowasaikoｰnomangadesu
```

