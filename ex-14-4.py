#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

c = input('请输入颜色单词首字母： ')
if c == 'b' or c == 'B':
    color('blue')
if c == 'r' or c == 'R':
    color('red')
if c == 'g' or c == 'G':
    color('green')
for i in range(200):
    forward(i)
    right(360 / 5 + 4)
done()
