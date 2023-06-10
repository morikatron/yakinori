# yakinori
Japanese Converter Kanji to Hiragana, Katakana, Latin alphabet.  
日本語の漢字を平仮名/カタカナ/ローマ字に変換するライブラリです。

# Test Environments（テスト環境）
```
Ubuntu18.04
python==3.8.16
```

## Install Mecab（Mecabのインストール）
### For Ubuntu（Ubuntuの場合）
```
$ sudo apt update
$ sudo apt install mecab libmecab-dev mecab-ipadic-utf8
```

## Install mecab-unidic-neologd（mecab-unidic-neologdのインストール）
```
$ git clone --depth 1 https://github.com/neologd/mecab-unidic-neologd.git
$ cd mecab-unidic-neologd
$ sudo ./install-mecab-unidic-neologd -n -y

# show installed unidic dictionary path
$ echo `mecab-config --dicdir`"/mecab-unidic-neologd"
> /usr/local/lib/mecab/dic/mecab-unidic-neologd
```

## Install yakinori（yakinoriのインストール）
```
$ pip install git+ssh://git@github.com/morikatron/yakinori.git
$ pip install yakinori # TODO:公開したらこちらにする
```

# How to use（使い方）
```python
from yakinori import Yakinori
yakinori = Yakinori(dic_path="path/to/mecab-unidic-neologd")
# example:
# yakinori = Yakinori(dic_path="/usr/local/lib/mecab/dic/mecab-unidic-neologd")

sentence = "今日はいい天気なので、外出したいですね。"
parsed_list = yakinori.get_parsed_list(sentence)

# convert to hiragana（平仮名に変換）
hiragana_sentence = yakinori.get_hiragana_sentence(parsed_list)
print(hiragana_sentence)
> きょーわいーてんきなので、がいしゅつしたいですね。

# convert to katakana（カタカナに変換）
katakana_sentence = yakinori.get_katakana_sentence(parsed_list)
print(katakana_sentence)
> キョーワイーテンキナノデ、ガイシュツシタイデスネ。

# convert to Latin alphabet（ローマ字に変換）
roma_sentence = yakinori.get_roma_sentence(parsed_list)
print(roma_sentence)
> kyoｰwaiｰtenkinanode､gaishutsushitaidesune｡
```

