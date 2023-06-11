"""
Created by hikaru.yamada@morikatron.co.jp
Copyright (c) 2023 Morikatron Inc. All rights reserved.
"""
import MeCab
import jaconv


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
        yomi_index = 0 if is_hatsuon else 1
        katakana_sentence = ""
        for mrph_result in parsed_list:
            if mrph_result[0] in ("EOS"):
                continue
            elif len(mrph_result) == 1:
                kana = mrph_result[0]
            elif mrph_result[yomi_index + 1] == "":
                kana = mrph_result[0]
            else:
                kana = mrph_result[yomi_index + 1]
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
