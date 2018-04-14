#!/usr/bin/env python3
# coding: utf-8
# File: viterbi.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-12

'''verterbi算法求解'''

def viterbi(obs, states, start_p, trans_p, emit_p):  # 维特比算法（一种递归算法）
    Min_Prob = 1e-10
    # 算法的局限在于训练语料要足够大，需要给每个词一个发射概率,.get(obs[0], 0)的用法是如果dict中不存在这个key,则返回0值
    V = [{}]
    result = list()
    for state in states:
        # 初始化t0时刻的隐藏状态概率
        V[0][state] = start_p[state] * emit_p[state].get(obs[0], Min_Prob)  # 在位置0，以y状态为末尾的状态序列的最大概率
    for t in range(1, len(obs)):
        # 记录从t1时刻开始的隐藏状态
        V.append({})
        for current_state in states:
            max_prob = max([V[t - 1][pre_state] * trans_p[pre_state].get(current_state, Min_Prob) * emit_p[current_state].get(obs[t], Min_Prob) for pre_state in states])
            V[t][current_state] = max_prob
    for vector in V:
        max_state = sorted(vector.items(), key=lambda asd: asd[1], reverse=True)[0][0]
        result.append(max_state)
    return result


