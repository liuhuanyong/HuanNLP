#!/usr/bin/env python3
# coding: utf-8
# File: crf_dep.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-13

import os
import sklearn_crfsuite
from sklearn.externals import joblib
from .feature_dep import *

class DEP:
    def __init__(self):
        self.model_path = '/'.join(os.path.abspath(__file__).split('/')[:-2]) + '/model/crf_dep_model.pkl'
        self.reldict_path = '/'.join(os.path.abspath(__file__).split('/')[:-2]) + '/model/rel_dict.txt'
        self.model = joblib.load(self.model_path)
        self.rel_dict = self.load_rel_dict(self.reldict_path)

    '''加载reldict'''
    def load_rel_dict(self, rel_dictpath):
        rel_dict = {}
        for line in open(rel_dictpath):
            line = line.strip().split('	')
            if not line:
                continue
            rel = line[0] + '@' + line[1]
            rel_name = line[-1]
            rel_dict[rel] = rel_name
        return rel_dict

    '''加载模型'''
    def load_model(self):
        return joblib.load(self.model_path)

    '''依存关系标准化'''
    def labelmodify(self, pos_list, word_list, labels):
        print(pos_list, word_list)
        print(len(pos_list))
        print(len(word_list))
        print(labels)

        rel_list = []
        for index in range(len(word_list)):
            current_word = word_list[index]
            current_pos = pos_list[index]
            center_dep = labels[index]
            if center_dep == '-1Root':
                center_word = 'Root'
                center_pos = '-'
                dist = 0
            else:
                dist = int(center_dep[:-1])
                target_index = index + dist
                if target_index == len(word_list):
                    target_index = index - 1

                if target_index == 0:
                    target_index = index + 1

                print(target_index)
                center_word = word_list[target_index]
                center_pos = pos_list[target_index]

            rel_list.append([current_word, current_pos, center_word, center_pos, dist])

        return rel_list

    '''依存关系分类'''
    def reltype_tag(self, rel_list):
        tagged_rellist = []
        for rel in rel_list:
            if rel[-1] > 0:
                key = rel[1][0] + '@' + rel[-2]
            else:
                key = rel[-2] + '@' +rel[1][0]
            value = self.rel_dict.get(key, 'na')
            tagged_rellist.append(rel[:-1] + [value])
            print(rel)
        return tagged_rellist

    '''依存句法分析'''
    def dep(self, word_list, pos_list):
        sent = []
        for index in range(len(word_list)):
            sent.append((word_list[index], pos_list[index], pos_list[index]))
        sent_reps = [feature_extract(sent)]
        labels = self.model.predict(sent_reps)[0]
        dep_data = self.labelmodify(pos_list, word_list, labels)
        dep_info = self.reltype_tag(dep_data)

        return dep_info
