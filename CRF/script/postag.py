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
class POSTAG:
    def __init__(self):
        self.model_path = '/'.join(os.path.abspath(__file__).split('/')[:-2]) + '/model/crf_pos_model.pkl'
        self.model = joblib.load(self.model_path)

    def postag(self, word_list):
        sent_reps = feature_extract(word_list)
        return self.model.predict(sent_reps)[0]

    # #测试
    # def test():
    #     import jieba
    #     model_path = '../model/crf_pos_model_40w_1.pkl'
    #     sent = '《我爱你》是根据韩国漫画家姜草的同名漫画改编的爱情电影，由秋昌民执导，李顺载，尹秀晶，宋在浩，金秀美，宋智孝，吴达秀，李文植等人出演。'
    #     #sent = '我爱你，你知道吗，我是刘焕勇，我来自北京语言大学，现在在中国科学院软件研究所工作'
    #     sent = '目前，这份书面道歉决议已经正式呈交中国驻纽约总领事章启月，得到了中方的书面回复，并于当地时间4月5日转呈陕西省文物交流中心。'
    #     #sent = '特朗普发表讲话又扔稿子:读第一段话就觉得无聊'
    #     #sent = '伟哉雄安，天下瞩目。“以疏解北京非首都功能为‘牛鼻子’推动京津冀协同发展，高起点规划、高标准建设雄安新区。'
    #     word_list = list(jieba.cut(sent))
    #     model = load_model(model_path)
    #     print(postag(word_list, model))
    #
    # test()
