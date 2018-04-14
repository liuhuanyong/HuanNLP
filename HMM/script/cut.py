#!/usr/bin/env python3
# coding: utf-8
# File: hmm_cut.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-3-26

from .viterbi import *
import os

class CUT:
    def __init__(self):
        self.current_path = '/'.join(os.path.abspath(__file__).split('/')[:-2])
        trans_path = self.current_path + '/model/hmm_cut_trans.model'
        emit_path = self.current_path + '/model/hmm_cut_emit.model'
        start_path = self.current_path + '/model/hmm_cut_start.model'
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

    '''分词主控函数'''
    def cut(self, sent):
        labels = viterbi(sent, ('B', 'M', 'E', 'S'), self.prob_start, self.prob_trans, self.prob_emit)
        return self.label2word(labels, sent)

# def test():
#     sent = '大连女子高铁直播声太大 被劝阻后狂飙日语怼乘警'
#     sent = '北京大学学生前来应聘'
#     sent = '新华网驻东京记者报道'
#     sent = '我们在野生动物园玩'
#     sent = '特朗普发表讲话又扔稿子:读了第一段就觉得无聊'
#     cuter = HmmCut()
#     seglist = cuter.cut(sent)
#     print(seglist)
#
# test()
