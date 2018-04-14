#!/usr/bin/env python3
# coding: utf-8
# File: hynlp.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-12
from CRF.CRF import *
from HMM.HMM import *
import re

class HuanNLP:
    def __init__(self, algorithm = 'CRF'):
        self.algorithm = algorithm
        print(self.algorithm)

    def sentsplit(self, text):
        sents = re.split(r"([。!！?？])", text.strip())
        sents.append("")
        sents = [item for item in ["".join(i) for i in zip(sents[0::2], sents[1::2])] if len(item) > 0]
        return sents

    def ner(self, text):
        if self.algorithm == 'CRF':
            return CRF().ner(text)
        elif self.algorithm == 'HMM':
            return HMM().ner(text)

    def cut(self, text):
        if self.algorithm == 'CRF':
            return CRF().cut(text)
        elif self.algorithm == 'HMM':
            return HMM().cut(text)

    def postag(self, text):
        if self.algorithm == 'CRF':
            return CRF().postag(text)
        elif self.algorithm == 'HMM':
            return HMM().postag(text)

    def dep(self, word_list, pos_list):
        return CRF().dep(word_list, pos_list)

    
    



