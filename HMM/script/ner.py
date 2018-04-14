#!/usr/bin/env python3
# coding: utf-8
# File: hmm_ner.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-7
from .viterbi import *
import os

class NER:
    def __init__(self):
        self.current_path = '/'.join(os.path.abspath(__file__).split('/')[:-2])
        trans_path = self.current_path + '/model/hmm_ner_trans.model'
        emit_path = self.current_path + '/model/hmm_ner_emit.model'
        start_path = self.current_path + '/model/hmm_ner_start.model'
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


    '''分词主控函数'''
    def ner(self, sent):
        state_list = ['nh-B','nh-M','nh-E',
                     'ns-B','ns-M','ns-E',
                     'ni-B','ni-M','ni-E',
                     'O'] #状态序列
        ner_list = viterbi(sent, state_list, self.prob_start, self.prob_trans, self.prob_emit)
        return self.label2word(ner_list, sent)
# '''
# def test():
#     '''
#     nh:人名，巴拉基列夫/nh
#         居伊/nh
#         鲍罗丁/nh
#         里姆斯基/nh
#         柯萨科夫/nh
#         穆索尔斯基/nh
#     ns：地名
#         昆仑山/ns
#         甘肃/ns
#         内蒙/ns
#         狼山/ns
#         广西/ns
#         花山/ns
#         云南/ns
#         沧源/ns
#     ni:机构名
#         黄埔军校/ni
#         德盛堂/ni
#         国民党/ni
#         中国工农红军/ni
#     '''
#     sent = '大连女子高铁直播声太大 被劝阻后狂飙日语怼乘警'
#     #sent = '''目前在自然语言处理技术中，中文处理技术比西文处理技术要落后很大一段距离，许多西文的处理方法中文不能直接采用，就是因为中文必需有分词这道工序。中文分词是其他中文信息处理的基础，搜索引擎只是中文分词的一个应用。'''
#     sent = '北京大学学生前来应聘'
#     #sent = '新华网驻东京记者报道'
#     #sent = '我们在野生动物园玩'
#     #sent = '特朗普发表讲话又扔稿子:读了第一段就觉得无聊'
#     sent = '''“订民主联合政府的施政纲领，业已成为必要，时机亦已成熟。国内广大民主人士业已有了此种要求，想二兄必有同感。但欲实现这一步骤，必须先邀集各民主党派、各人民团体的代表开一个会议。在这个会议上，讨论并决定上述问题。此项会议似宜定名为政治协商会议。一切反美帝反蒋党的民主党派、人民团体，均可派代表参加。不属于各民主党派各人民团体的反美帝反蒋党的某些社会贤达，亦可被邀参加此项会议。此项会议的决定，必须求得到会各主要民主党派及各人民团体的共同一致，并尽可能求得全体一致。会议的地点，提议在哈尔滨。会议的时间，提议在今年秋季。并提议由中国国民党革命委员会、中国民主同盟中央执行委员会、中国共产党中央委员会于本月内发表三党联合声明，以为号召。此项联合声明，弟已拟了一个草案，另件奉陈。以上诸点是否适当，敬请二兄详加考虑，予以指教。三党联合声明内容文字是否适当，抑或不限于三党，加入其他民主党派及重要人民团体联署发表，究以何者适宜，统祈赐示。兹托潘汉年同志进谒二兄。二兄有所指示，请交汉年转达，不胜感幸。'''
#     sent = '''毛泽东提笔致信避居香港的中国国民党革命委员会主席李济深（字任潮）和中国民主同盟中央常务委员、在香港主持盟务工作的沈钧儒（号衡山），以协商的口吻具体提出了召开政治协商会议的时间、地点、参会党派和原则、实施步骤等，对中共中央“五一口号”第五条作了进一步的阐释。人民出版社1996年版《毛泽东文集》第五卷收录了这封信，内容如下：任潮、衡山两先生：'''
#     sent = '''刘焕勇今天去了北京工作，在中国科学院软件研究所工作
#     '''
#     hmmner = HmmNer()
#     ner_dict = hmmner.ner(sent)
#     print(ner_dict)
#
# test()