#!/usr/bin/env python3
# coding: utf-8
# File: test.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-12
import huannlp

def test():
    nlp = huannlp.HuanNLP('CRF')
    text = '''刘焕勇硕士毕业于北京语言大学，目前在中国科学院软件研究所工作'''
    text = '一是新类型性能灌注树脂的创新开发;'
    words = nlp.cut(text)
    print('words', words)
    postags = nlp.postag(words)
    print('postags', postags)
    ners = nlp.ner(text)
    print('ners', ners)
    deps = nlp.dep(words, postags)
    print('deps',deps)
test()

''''
CRF
words ['刘焕勇', '硕士', '毕业于', '北京', '语言', '大学', '，', '目前', '在', '中国科学院', '软件', '研究', '所', '工作']
postags ['n', 'n', 'v', 'ns', 'n', 'n', 'w', 'nt', 'p', 'ni', 'n', 'v', 'u', 'n']
ners {'LOC': [], 'TIM': ['目前'], 'PER': ['刘焕勇'], 'ORG': ['中国科学院', '北京语言大学']}

HMM
words ['刘焕勇', '硕士', '毕业', '于', '北京', '语言', '大学', '，', '目前', '在', '中', '国', '科学', '院', '软', '件', '研究', '所', '工作']
postags ['r', 'n', 'v', 'p', 'ns', 'n', 'n', 'w', 'nt', 'p', 'nd', 'n', 'n', 'n', 'a', 'n', 'v', 'u', 'n']
ners {'TIM': [], 'PER': ['刘焕勇'], 'LOC': [], 'ORG': []}
'''
