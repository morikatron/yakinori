# yakinori
Japanese Converter Kanji to Hiragana, Katakana, Latin alphabet.  
日本語の漢字を平仮名/カタカナ/ローマ字に変換するライブラリです。

# Test Environments（テスト環境）
```
Ubuntu18.04
python==3.8
```

## Install Mecab（Mecabのインストール）
### For Ubuntu（Ubuntuの場合）
```
sudo apt update
sudo apt install mecab libmecab-dev mecab-ipadic-utf8
```

## Install mecab-unidic-neologd（mecab-unidic-neologdのインストール）
```
git clone --depth 1 https://github.com/neologd/mecab-unidic-neologd.git
cd mecab-unidic-neologd
sudo ./install-mecab-unidic-neologd -n -y

# show installed unidic dictionary path
$ echo `mecab-config --dicdir`"/mecab-unidic-neologd"
> /usr/local/lib/mecab/dic/mecab-unidic-neologd
```

# How to use（使い方）
```python
yakinori = Yakinori()
yakinori = Yakinori("/usr/local/lib/mecab/dic/mecab-unidic-neologd")
sentence = "今日はいい天気ですね。"
parsed_list = yakinori.get_parsed_list(sentence)

# convert to hiragana（平仮名に変換）
hiragana_sentence = yakinori.get_hiragana_sentence(parsed_list)
print(hiragana_sentence)

# convert to katakana（カタカナに変換）
katakana_sentence = yakinori.get_katakana_sentence(parsed_list)
print(katakana_sentence)

# convert to Latin alphabet（ローマ字に変換）
roma_sentence = yakinori.get_roma_sentence(parsed_list)
print(roma_sentence)
```

