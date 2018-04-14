#!/usr/bin/env python3
# coding: utf-8
# File: hmm_cut.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-3-26
#from viterbi import *
from .viterbi import *
import os

class POSTAG:
    def __init__(self):
        self.current_path = '/'.join(os.path.abspath(__file__).split('/')[:-2])
        trans_path = self.current_path + '/model/hmm_pos_trans.model'
        emit_path = self.current_path + '/model/hmm_pos_emit.model'
        start_path = self.current_path + '/model/hmm_pos_start.model'
        self.prob_trans = self.load_model(trans_path)
        self.prob_emit = self.load_model(emit_path)
        self.prob_start = self.load_model(start_path)

    '''加载模型'''
    def load_model(self, model_path):
        f = open(model_path, 'r')
        a = f.read()
        word_dict = eval(a)
        f.close()
        return word_dict

    # 分词主控函数
    def postag(self, word_list):
        state_list = ['n', 'nt', 'nd', 'nl', 'nh', 'nhf', 'ns', 'nhs',
                      'nn', 'ni', 'nz', 'v', 'vd', 'vl', 'vu',
                      'a', 'f', 'm', 'mq', 'q', 'd', 'r',
                      'p', 'c', 'u', 'e', 'o', 'i', 'j',
                      'h', 'k', 'g', 'x', 'w', 'ws', 'wu']  # 状态序列

        pos_list = viterbi(word_list, state_list, self.prob_start, self.prob_trans, self.prob_emit)
        return pos_list

'''
def test():
    import jieba
    word_list = ['我', '是', '中国', '人']
    s = '特朗普发表讲话又扔稿子:读了第一段就觉得无聊'
    word_list = list(jieba.cut(s))
    print(word_list)
    #word_list = ['今天', '天气', '特别', '好']
    postager = HmmPostag()
    pos_list, result = postager.postag(word_list)
    print(result)

test()
'''
