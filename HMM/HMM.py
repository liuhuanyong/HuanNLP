#!/usr/bin/env python3
# coding: utf-8
# File: hmm.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-12

from .script.cut import *
from .script.ner import *
from .script.postag import *

class HMM:
    def __init__(self):
        pass

    def postag(self, word_list):
        postager = POSTAG()
        return postager.postag(word_list)

    def ner(self, sent):
        nerer = NER()
        return nerer.ner(sent)

    def cut(self, sent):
        cuter = CUT()
        return cuter.cut(sent)


# HMMer = HMM()
# sent =  '目前，这份书面道歉决议已经正式呈交中国驻纽约总领事章启月，得到了中方的书面回复，并于当地时间4月5日转呈陕西省文物交流中心。'
# seg_list = HMMer.cut(sent)
# ner_dict = HMMer.ner(sent)
# pos_list = HMMer.postag(seg_list)
#
# print(seg_list)
# print(pos_list)
# print(ner_dict)