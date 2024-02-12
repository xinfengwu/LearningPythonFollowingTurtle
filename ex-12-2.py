#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = ''  # 字符串变量初始为空
# 将1到30间的所有奇数转化为字符串，拼接到s中
for i in range(29, 0, -2):
    s = str(i) + '、' + s
print('1到30之间的奇数有： ' + s + '。')  # 输出s
