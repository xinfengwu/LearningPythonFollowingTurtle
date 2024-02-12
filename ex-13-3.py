#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

c = input('请输入颜色单词首字母： ')
if c == 'b':
    color('blue')
for i in range(200):
    forward(i)
    right(360 / 5 + 4)
done()
