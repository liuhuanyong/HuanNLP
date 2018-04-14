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
class NER:
    def __init__(self):
        self.model_path = '/'.join(os.path.abspath(__file__).split('/')[:-2]) + '/model/crf_ner_model.pkl'
        self.model = joblib.load(self.model_path)

    #将序列标记转换为标记结果
    def label2word(self, labels, sent):
        per = []
        loc = []
        org = []
        tim = []
        tim_tmp = []
        loc_tmp = []
        per_tmp = []
        org_tmp = []
        ner_dict = {}
        for index in range(len(labels)):
            label = labels[index]
            word = sent[index]
            pair = [word, label]

            if label == 'ns-B':
                if loc_tmp and 'ns-E' in loc_tmp:
                    loc.append(loc_tmp)
                loc_tmp = []
                loc_tmp.extend(pair)

            elif label == 'ns-M':
                loc_tmp.extend(pair)
            elif label == 'ns-E':
                loc_tmp.extend(pair)
                if 'ns-B' in loc_tmp:
                    loc.append(loc_tmp)
                loc_tmp = []

            if label == 'nh-B':
                if per_tmp and 'nh-E' in per_tmp:
                    per.append(per_tmp)
                per_tmp = []
                per_tmp.extend(pair)
            elif label == 'nh-M':
                per_tmp.extend(pair)
            elif label == 'nh-E':
                per_tmp.extend(pair)
                if 'nh-B' in per_tmp:
                    per.append(per_tmp)
                per_tmp = []

            if label == 'ni-B':
                if org_tmp and 'ni-E' in org_tmp:
                    org.append(org_tmp)
                org_tmp = []
                org_tmp.extend(pair)
            elif label == 'ni-M':
                org_tmp.extend(pair)
            elif label == 'ni-E':
                org_tmp.extend(pair)
                if 'ni-B' in org_tmp:
                    org.append(org_tmp)
                org_tmp = []

            if label == 'nt-B':
                if tim_tmp and 'nt-E' in tim_tmp:
                    tim.append(tim_tmp)
                tim_tmp = []
                tim_tmp.extend(pair)
            elif label == 'nt-M':
                tim_tmp.extend(pair)
            elif label == 'nt-E':
                tim_tmp.extend(pair)
                if 'nt-B' in tim_tmp:
                    tim.append(tim_tmp)
                tim_tmp = []

        LOC = [''.join([loc_ for loc_ in [sub_item for sub_item in item if item.index(sub_item) % 2 == 0]]) for item in loc
               if item]
        PER = [''.join([per_ for per_ in [sub_item for sub_item in item if item.index(sub_item) % 2 == 0]]) for item in per
               if item]
        ORG = [''.join([org_ for org_ in [sub_item for sub_item in item if item.index(sub_item) % 2 == 0]]) for item in org
               if item]
        TIM = [''.join([org_ for org_ in [sub_item for sub_item in item if item.index(sub_item) % 2 == 0]]) for item in tim
               if item]

        ner_dict['LOC'] = list(set(LOC))
        ner_dict['ORG'] = list(set(ORG))
        ner_dict['PER'] = list(set(PER))
        ner_dict['TIM'] = list(set(TIM))
        return ner_dict

    def ner(self, sent):
        sent_reps = feature_extract(sent)
        labels = self.model.predict(sent_reps)[0]
        return self.label2word(labels, sent)

# #测试
# def test():
#     model_path = '../model/crf_ner_model_12w_1.pkl'
#     sent = '《我爱你》是根据韩国漫画家姜草的同名漫画改编的爱情电影，由秋昌民执导，李顺载，尹秀晶，宋在浩，金秀美，宋智孝，吴达秀，李文植等人出演。'
#     sent = '我爱你，你知道吗，我是刘焕勇，我来自北京语言大学，现在在中国科学院软件研究所工作'
#     sent = '目前，这份书面道歉决议已经正式呈交中国驻纽约总领事章启月，得到了中方的书面回复，并于当地时间4月5日转呈陕西省文物交流中心。'
#     sent = '特朗普发表讲话又扔稿子:读第一段话就觉得无聊'
#     #sent = '伟哉雄安，天下瞩目。“以疏解北京非首都功能为‘牛鼻子’推动京津冀协同发展，高起点规划、高标准建设雄安新区。'
#     model = load_model(model_path)
#     print(ner(sent, model))
#
# test()
