"""
Created by hikaru.yamada@morikatron.co.jp
Copyright (c) 2023 Morikatron Inc. All rights reserved.
"""
import MeCab
import jaconv


class Yakinori:
    def __init__(self, dic_path):
        self.tagger = MeCab.Tagger(f"-d {dic_path}")

    def get_parsed_list(self, sentence):
        parsed_result = self.tagger.parse(sentence)
        return [p.split("\t") for p in parsed_result.split("\n")][:-2]

    def get_katakana_sentence(self, parsed_list):
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
            katakana_sentence += kana
        return katakana_sentence

    def get_hiragana_sentence(self, parsed_list):
        katakana_sentence = self.get_katakana_sentence(parsed_list)
        hiragana_sentence = jaconv.kata2hira(katakana_sentence)
        return hiragana_sentence

    def get_roma_sentence(self, parsed_list):
        katakana_sentence = self.get_katakana_sentence(parsed_list)
        roma_sentence = jaconv.kata2alphabet(katakana_sentence)
        roma_sentence = jaconv.z2h(roma_sentence)
        return roma_sentence
