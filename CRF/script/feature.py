#!/usr/bin/env python3
# coding: utf-8
# File: feature_extract.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-9
import sklearn_crfsuite
from sklearn_crfsuite import metrics
from sklearn.externals import joblib

def isPu(char):
    punctuation = [u'，', u'。', u'？', u'！', u'；', u'－－', u'、', u'——', u'（', u'）', u'《', u'》', u'：', u'“', u'”', u'’',u'‘']
    if char in punctuation:
        return '1'
    else:
        return '0'

def get_class(char):
    zh_num = [u'零', u'○', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十', u'百', u'千', u'万']
    ar_num = [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'.', u'０', u'１', u'２', u'３', u'４', u'５',
                  u'６', u'７', u'８', u'９']
    date = [u'日', u'年', u'月']
    letter = ['a', 'b', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if char in zh_num or char in ar_num:
        return '1'
    elif char in date:
        return '2'
    elif char in letter:
        return '3'
    else:
        return '4'

'''特征提取'''
def feature_extract(sent):
    sent_rep = []
    x_train = []
    features = list()
    if len(sent) == 1:
        features.append(['_', '_', sent[0], '_', '_'])
    elif len(sent) == 2:
        features.append(['_', '_', sent[0], sent[1], '_'])
        features.append(['_', sent[0], sent[1], '_', '_'])
    elif len(sent) == 3:
        features.append(['_', '_', sent[0], sent[1], sent[2]])
        features.append(['_', sent[0], sent[1], sent[2], '_'])
        features.append([sent[0], sent[1], sent[2], '_', '_'])
    elif len(sent) > 3:
        for index in range(len(sent)):
            C_0 = sent[index]
            if index == 0:
                C_2_ = '_'
                C_1_ = '_'
                C_1 = sent[index + 1]
                C_2 = sent[index + 2]
            elif index == 1:
                C_2_ = '_'
                C_1_ = sent[0]
                C_1 = sent[index + 1]
                C_2 = sent[index + 2]
            elif index == len(sent) - 1:
                C_2 = '_'
                C_1 = '_'
                C_1_ = sent[index - 1]
                C_2_ = sent[index - 2]
            elif index == len(sent) - 2:
                C_2 = '_'
                C_1 = sent[index + 1]
                C_2_ = sent[index - 2]
                C_1_ = sent[index - 1]
            else:
                C_2_ = sent[index - 2]
                C_1_ = sent[index - 1]
                C_1 = sent[index + 1]
                C_2 = sent[index + 2]
            features.append([C_2_, C_1_, C_0, C_1, C_2])

    for feature in features:
        C_2_ = feature[0]
        C_1_ = feature[1]
        C_0 = feature[2]
        C_1 = feature[3]
        C_2 = feature[4]

        x_rep = {
                'C-2':C_2_,
                'C-1': C_1_,
                'C0': C_0 ,
                'C1': C_1,
                'C2' : C_2,
                'Pu' : isPu(C_0),
                'Tc-2' : get_class(C_2_),
                'Tc-1' : get_class(C_1_),
                'Tc0' : get_class(C_0) ,
                'Tc1' : get_class(C_1),
                'Tc2' : get_class(C_2),
            }

        # x_rep = {'C-2': C_2_,
        #      'C-1': C_1_,
        #      'C0': C_0,
        #      'C1': C_1,
        #      'C2': C_2,
        #      'C-2C-1': C_2_ + C_1_,
        #      'C-1C0': C_1 + C_0,
        #      'C0C1': C_0 + C_1,
        #      'C1C2': C_1 + C_2,
        #      'C-1C1': C_1_ + C_1,
        #      'Pu': isPu(C_0),
        #      'Tc-2': get_class(C_2_),
        #      'Tc-1': get_class(C_1_),
        #      'Tc0': get_class(C_0),
        #      'Tc1': get_class(C_1),
        #      'Tc2': get_class(C_2),
        #      }

        x_train.append(x_rep)
        sent_rep.append(x_train)

    return sent_rep

# def test():
#     sent = '我是中国人，我热爱我的祖国'
#     sent_rep = feature_extract(sent)
#     print(sent_rep)
#
# test()

