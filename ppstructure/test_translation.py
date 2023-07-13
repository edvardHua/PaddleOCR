# -*- coding: utf-8 -*-
# @Time : 2023/7/11 22:36
# @Author : zihua.zeng
# @File : translate_test.py

import re
import json
import requests


def en_to_cn(en_str):
    while True:
        url = 'http://104.197.70.137:8000'
        myobj = {"prompt": "%s . 翻译成中文" % en_str, "history": []}
        res = requests.post(url, json=myobj)
        cl = count_characters(en_str)
        if not res.ok:
            return en_str
        res = json.loads(res.text)
        if res['status'] != 200:
            return en_str
        rl = count_characters(res['response'])
        # 偶然会返回很长的字符串，是错误的
        # 这里简单的做一下过滤
        # TODO: 后续查一下造成这个问题的原因
        if sum(rl) < 6 * sum(cl):
            break

    return res['response']


def count_characters(string):
    pattern_en = r'[a-zA-Z]'
    pattern_digit = r'\d'
    pattern_cn = r'[\u4e00-\u9fff]'
    pattern_punct = r'[\u2000-\u206F\u3000-\u303F\uFF00-\uFFEF\!\"#\$%&\'\(\)\*\+,\-\./:;<=>\?@\[\\\]\^_`\{\|\}~]'

    count_en = len(re.findall(pattern_en, string))
    count_digit = len(re.findall(pattern_digit, string))
    count_cn = len(re.findall(pattern_cn, string))
    count_punct = len(re.findall(pattern_punct, string))

    return count_en, count_digit, count_cn, count_punct
