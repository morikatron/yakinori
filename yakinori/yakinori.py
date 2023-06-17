"""
Created by hikaru.yamada@morikatron.co.jp
Copyright (c) 2023 Morikatron Inc. All rights reserved.
"""
import re

import MeCab
import jaconv

re_full_kanji = re.compile(r"^[\u4E00-\u9FFF]+$")
re_head_kanji = re.compile(r"^(?P<kanji>[\u4E00-\u9FFF])(?P<kana>.+)")
re_katakana = re.compile(r"^[\u30A0-\u30FF]+$")


class Yakinori:
    def __init__(self, dic_path: str = ''):
        assert isinstance(dic_path, str), 'dic_path must be str'
        mecab_option = ''
        if dic_path != '':
            mecab_option = f"-d {dic_path}"
        self.tagger = MeCab.Tagger(mecab_option)

    def get_parsed_list(self, sentence: str) -> list:
        """get mecab parsed list

        Args:
            sentence (str): input sentence

        Returns:
            list: parsed_list using mecab tagger
        """
        parsed_result = self.tagger.parse(sentence)
        return [p.split("\t") for p in parsed_result.split("\n")][:-2]

    def get_katakana_sentence(self, parsed_list: list, is_hatsuon=False) -> str:
        """get katakana sentence from parsed_list

        Args:
            parsed_list (list): parsed_list using mecab tagger
            is_hatsuon (bool, optional): If you need to get hatsuon, set is_hatsuon=True. Defaults to False.

        Returns:
            str: katakana sentence
        """
        katakana_sentence = ""
        for mrph_result in parsed_list:
            if mrph_result[0] in ("EOS"):
                continue
            elif len(mrph_result) == 1:
                kana = mrph_result[0]
            elif mrph_result[1] == "":
                kana = mrph_result[0]
            else:
                kana = mrph_result[1]
                if not is_hatsuon:
                    matched_head_kanji = re_head_kanji.match(mrph_result[0])
                    if re_full_kanji.match(mrph_result[0]):
                        kana = jaconv.hira2kata(mrph_result[2])
                    elif re_katakana.match(jaconv.hira2kata(mrph_result[0])):
                        kana = jaconv.hira2kata(mrph_result[0])
                    elif (len(mrph_result) > 4) and (mrph_result[4][:7] == "名詞-固有名詞"):
                        kana = mrph_result[2]
                    elif matched_head_kanji:
                        __tail_kana = matched_head_kanji.group("kana")
                        kana = jaconv.hira2kata(mrph_result[2][:-len(__tail_kana)]) + jaconv.hira2kata(__tail_kana)
                    elif jaconv.hira2kata(mrph_result[0]) == mrph_result[2]:
                        kana = jaconv.hira2kata(mrph_result[0])
            katakana_sentence += kana
        return katakana_sentence

    def get_hiragana_sentence(self, parsed_list, is_hatsuon=False):
        """get katakana sentence from parsed_list

        Args:
            parsed_list (list): parsed_list using mecab tagger
            is_hatsuon (bool, optional): If you need to get hatsuon, set is_hatsuon=True. Defaults to False.

        Returns:
            str: hiragana sentence
        """
        katakana_sentence = self.get_katakana_sentence(parsed_list, is_hatsuon)
        hiragana_sentence = jaconv.kata2hira(katakana_sentence)
        return hiragana_sentence

    def get_roma_sentence(self, parsed_list, is_hatsuon=False):
        """get Latin alphabet sentence from parsed_list

        Args:
            parsed_list (list): parsed_list using mecab tagger
            is_hatsuon (bool, optional): If you need to get hatsuon, set is_hatsuon=True. Defaults to False.

        Returns:
            str: Latin alphabet sentence
        """
        katakana_sentence = self.get_katakana_sentence(parsed_list, is_hatsuon)
        roma_sentence = jaconv.kata2alphabet(katakana_sentence)
        roma_sentence = jaconv.z2h(roma_sentence)
        roma_sentence = roma_sentence.translate(str.maketrans({"､": ",", "｡": "."}))
        return roma_sentence
