#!/usr/bin/env python3
# coding: utf-8
# File: segment.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-9
import sklearn_crfsuite
from sklearn_crfsuite import metrics
from sklearn.externals import joblib
from .feature import *
import os
class CUT:
    def __init__(self):
        self.model_path = '/'.join(os.path.abspath(__file__).split('/')[:-2]) + '/model/crf_cut_model.pkl'
        self.model = joblib.load(self.model_path)

    #将序列标记转换为标记结果
    def label2word(self, labels, sent):
        labellist = []
        tmp = []
        for index in range(len(labels)):
            word = sent[index]
            tag = labels[index]
            if tag == 'S':
                if tmp:
                    labellist.append(tmp)
                tmp = [word]
                labellist.append(tmp)
                tmp = []
            elif tag == 'B':
                if tmp:
                    labellist.append(tmp)
                tmp = []
                tmp.append(word)
            elif tag == 'M':
                tmp.append(word)
            elif tag == 'E':
                tmp.append(word)
                labellist.append(tmp)
                tmp = []
        return [''.join(tmp) for tmp in labellist]

    #分词主函数
    def cut(self, sent):
        sent_reps = feature_extract(sent)
        labels = self.model.predict(sent_reps)[0]
        return self.label2word(labels, sent)

# #测试
# def test():
#     model_path =
#     sent = '《我爱你》是根据韩国漫画家姜草的同名漫画改编的爱情电影，由秋昌民执导，李顺载，尹秀晶，宋在浩，金秀美，宋智孝，吴达秀，李文植等人出演。'
#     #sent = '我爱你，你知道吗，我是刘焕勇，我来自北京语言大学，现在在中国科学院软件研究所工作'
#     sent = '目前，这份书面道歉决议已经正式呈交中国驻纽约总领事章启月，得到了中方的书面回复，并于当地时间4月5日转呈陕西省文物交流中心。'
#     #sent = '特朗普发表讲话又扔稿子:读第一段话就觉得无聊'
#     #sent = '伟哉雄安，天下瞩目。“以疏解北京非首都功能为‘牛鼻子’推动京津冀协同发展，高起点规划、高标准建设雄安新区。'
#     model = load_model(model_path)
#     print(cut(sent, model))
#
# test()