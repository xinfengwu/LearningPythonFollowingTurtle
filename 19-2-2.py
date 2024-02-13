#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
speed(0)
colors = []
for i in range(4):
    c = input('请输入颜色英文单词：')
    colors.append(c)
for i in range(150):
    index = i % 4
    color(colors[index])
    forward(i)
    right(91)
hideturtle()
done()
