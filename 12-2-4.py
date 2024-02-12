#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = ''  # 字符串变量初始为空
# 将0到20间的所有偶数转化为字符串，拼接到s中
for i in range(0, 21, 2):
    s = s + str(i) + ' '
print(s)  # 输出s
