# yakinori
Japanese REAMED is here.  
https://github.com/morikatron/yakinori/blob/main/README_ja.md

Japanese Converter Kanji to Hiragana, Katakana, Latin alphabet.  

You can get the reading and pronunciation of Japanese sentences based on mecab-unidic-NEologd.  

## Test Environments
```
Ubuntu18.04
python==3.8.16
```

## Install
There are two options to install.
- Install Mecab and mecab-unidic-NEologd in your own environment  
- Use Docker


### Your Own Environment
#### For Ubuntu
##### Install Mecab
```bash
$ sudo apt update
$ sudo apt install mecab libmecab-dev mecab-ipadic-utf8
```

##### Install mecab-unidic-NEologd
```bash
$ git clone --depth 1 https://github.com/neologd/mecab-unidic-neologd.git
$ cd mecab-unidic-neologd
$ sudo ./bin/install-mecab-unidic-neologd -n -y

# show installed mecab-unidic-NEologd dictionary path
$ echo `mecab-config --dicdir`"/mecab-unidic-neologd"
> /usr/local/lib/mecab/dic/mecab-unidic-neologd

# If you want to make mecab-unidic-NEologd as defalut dictionary, run commands below.
$ echo "dicdir = `mecab-config --dicdir`/mecab-unidic-neologd" | sudo tee /etc/mecabrc
$ sudo cp /etc/mecabrc /usr/local/etc

```

##### Install yakinori
```bash
$ pip install yakinori
```

##### You can update the recent mecab-unidic-NEologd
```bash
$ sudo ./bin/install-mecab-unidic-neologd -n -y
$ echo "dicdir = `mecab-config --dicdir`/mecab-unidic-neologd" | sudo tee /etc/mecabrc
$ sudo cp /etc/mecabrc /usr/local/etc
```

#### Use Docker
```bash
$ docker pull morikayamada/yakinori
```

## How to use
### Import
```python
>>> from yakinori import Yakinori
```

### create Instance
#### Installed on your Own Environment
- If you made mecab-unidic-NEologd as defalut dictionary, you don't need to add dic_path.  
```python
>>> yakinori = Yakinori()
```
- If you did not make mecab-unidic-NEologd as defalut dictionary, add dic_path.  
```python
>>> yakinori = Yakinori(dic_path='path/to/mecab-unidic-NEologd') 
```
#### Using Docker
If you use Docker, you don't need to add dic_path.  
```python
>>> yakinori = Yakinori()
```

### Parse Sentence
```python
>>> sentence = "幽☆遊☆白書は最高の漫画です"
>>> parsed_list = yakinori.get_parsed_list(sentence)
```

### Get Reading
```python
# convert to hiragana
>>> hiragana_sentence = yakinori.get_hiragana_sentence(parsed_list)
>>> print(hiragana_sentence)
ゆうゆうはくしょはさいこうのまんがです

# convert to katakana
>>> katakana_sentence = yakinori.get_katakana_sentence(parsed_list)
>>> print(katakana_sentence)
ユウユウハクショハサイコウノマンガデス

# convert to Latin alphabet
>>> roma_sentence = yakinori.get_roma_sentence(parsed_list)
>>> print(roma_sentence)
yuuyuuhakushohasaikounomangadesu
```

### Get Pronunciation
```python
# convert to hiragana
>>> hiragana_sentence = yakinori.get_hiragana_sentence(parsed_list, is_hatsuon=True)
>>> print(hiragana_sentence)
ゆーゆーはくしょわさいこーのまんがです

# convert to katakana
>>> katakana_sentence = yakinori.get_katakana_sentence(parsed_list, is_hatsuon=True)
>>> print(katakana_sentence)
ユーユーハクショワサイコーノマンガデス

# convert to Latin alphabet
>>> roma_sentence = yakinori.get_roma_sentence(parsed_list, is_hatsuon=True)
>>> print(roma_sentence)
yuｰyuｰhakushowasaikoｰnomangadesu
```

