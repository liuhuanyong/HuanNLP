#!/usr/bin/env python3
# coding: utf-8
# File: feature_extract.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-13

'''句法特征提取'''
def feature_extract(sample_infos):
    if len(sample_infos) == 1:
        w0 = sample_infos[0][0]
        c0 = sample_infos[0][1]
        p0 = sample_infos[0][2]
        sent_rep = [{
            'w-1': '_',
            'c-1': '_',
            'p-1': '_',

            'w-2': '_',
            'c-2': '_',
            'p-2': '_',

            'w0': w0,
            'c0': c0,
            'p0': p0,

            'w+1': '_',
            'c+1': '_',
            'p+1': '_',

            'w+2': '_',
            'c+2': '_',
            'p+2': '_',
        }]

    elif len(sample_infos) == 2:
        sent_rep = [{
            'w-1': '_',
            'c-1': '_',
            'p-1': '_',

            'w-2': '_',
            'c-2': '_',
            'p-2': '_',

            'w0': sample_infos[0][0],
            'c0': sample_infos[0][1],
            'p0': sample_infos[0][2],

            'w+1': '_',
            'c+1': '_',
            'p+1': '_',
            'w+2': '_',
            'c+2': '_',
            'p+2': '_',
        },
        {
            'w-1': sample_infos[0][0],
            'c-1': sample_infos[0][1],
            'p-1': sample_infos[0][2],

            'w-2': '_',
            'c-2': '_',
            'p-2': '_',

            'w0': sample_infos[1][0],
            'c0': sample_infos[1][1],
            'p0': sample_infos[1][2],

            'w+1': '_',
            'c+1': '_',
            'p+1': '_',

            'w+2': '_',
            'c+2': '_',
            'p+2': '_',

        }
        ]
    elif len(sample_infos) == 3:
        sent_rep = [{
            'w-1': '_',
            'c-1': '_',
            'p-1': '_',

            'w-2': '_',
            'c-2': '_',
            'p-2': '_',

            'w0': sample_infos[0][0],
            'c0': sample_infos[0][1],
            'p0': sample_infos[0][2],

            'w+1': '_',
            'c+1': '_',
            'p+1': '_',

            'w+2': '_',
            'c+2': '_',
            'p+2': '_',
        },

        {
            'w-1': sample_infos[0][0],
            'c-1': sample_infos[0][1],
            'p-1': sample_infos[0][2],

            'w-2': '_',
            'c-2': '_',
            'p-2': '_',

            'w0': sample_infos[1][0],
            'c0': sample_infos[1][1],
            'p0': sample_infos[1][2],

            'w+1': sample_infos[2][0],
            'c+1': sample_infos[2][1],
            'p+1': sample_infos[2][2],

            'w+2': '_',
            'c+2': '_',
            'p+2': '_',

        },

        {
            'w-1': sample_infos[1][0],
            'c-1': sample_infos[1][1],
            'p-1': sample_infos[1][2],

            'w-2': sample_infos[0][0],
            'c-2': sample_infos[0][1],
            'p-2': sample_infos[0][2],

            'w0': sample_infos[2][0],
            'c0': sample_infos[2][1],
            'p0': sample_infos[2][2],

            'w+1': '_',
            'c+1': '_',
            'p+1': '_',
            'w+2': '_',
            'c+2': '_',
            'p+2': '_',

        }
        ]

    else:
        sent_rep = []
        for index in range(len(sample_infos)):
            w0 = sample_infos[index][0]
            c0 = sample_infos[index][1]
            p0 = sample_infos[index][2]
            if index == 0:
                x = {
                    'w-1': '_',
                    'c-1': '_',
                    'p-1': '_',

                    'w-2': '_',
                    'c-2': '_',
                    'p-2': '_',

                    'w0': w0,
                    'c0': c0,
                    'p0': p0,

                    'w+1': sample_infos[index + 1][0],
                    'c+1': sample_infos[index + 1][1],
                    'p+1': sample_infos[index + 1][2],

                    'w+2': sample_infos[index + 2][0],
                    'c+2': sample_infos[index + 2][1],
                    'p+2': sample_infos[index + 2][2],
                }
            elif index == 1:
                x = {
                    'w-1': sample_infos[index - 1][0],
                    'c-1': sample_infos[index - 1][1],
                    'p-1': sample_infos[index - 1][2],

                    'w-2': '_',
                    'c-2': '_',
                    'p-2': '_',

                    'w0': w0,
                    'c0': c0,
                    'p0': p0,

                    'w+1': sample_infos[index + 1][0],
                    'c+1': sample_infos[index + 1][1],
                    'p+1': sample_infos[index + 1][2],

                    'w+2': sample_infos[index + 2][0],
                    'c+2': sample_infos[index + 2][1],
                    'p+2': sample_infos[index + 2][2],
                }
            elif index == len(sample_infos) -1:
                x = {
                    'w-1': sample_infos[index - 1][0],
                    'c-1': sample_infos[index - 1][1],
                    'p-1': sample_infos[index - 1][2],

                    'w-2': sample_infos[index - 2][0],
                    'c-2': sample_infos[index - 2][1],
                    'p-2': sample_infos[index - 2][2],

                    'w0': w0,
                    'c0': c0,
                    'p0': p0,

                    'w+1': '_',
                    'c+1': '_',
                    'p+1': '_',

                    'w+2': '_',
                    'c+2': '_',
                    'p+2': '_',
                }

            elif index == len(sample_infos) -2:
                x = {
                    'w-1': sample_infos[index - 1][0],
                    'c-1': sample_infos[index - 1][1],
                    'p-1': sample_infos[index - 1][2],

                    'w-2': sample_infos[index - 2][0],
                    'c-2': sample_infos[index - 2][1],
                    'p-2': sample_infos[index - 2][2],

                    'w0': w0,
                    'c0': c0,
                    'p0': p0,

                    'w+1': sample_infos[index + 1][0],
                    'c+1': sample_infos[index + 1][1],
                    'p+1': sample_infos[index + 1][2],

                    'w+2': '_',
                    'c+2': '_',
                    'p+2': '_',
                }

            else:
                x = {
                    'w-1': sample_infos[index - 1][0],
                    'c-1': sample_infos[index - 1][1],
                    'p-1': sample_infos[index - 1][2],

                    'w-2': sample_infos[index - 2][0],
                    'c-2': sample_infos[index - 2][1],
                    'p-2': sample_infos[index - 2][2],

                    'w0': w0,
                    'c0': c0,
                    'p0': p0,

                    'w+1': sample_infos[index + 1][0],
                    'c+1': sample_infos[index + 1][1],
                    'p+1': sample_infos[index + 1][2],

                    'w+2': sample_infos[index + 2][0],
                    'c+2': sample_infos[index + 2][1],
                    'p+2': sample_infos[index + 2][2],
                }

            sent_rep.append(x)

    return sent_rep


