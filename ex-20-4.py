#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
speed(0)
# 绘制长方形
for i in range(2):
    forward(5)
    right(90)
    forward(100)
    right(90)
# 绘制圆
for i in range(100):
    forward(5)
    right(-3.6)

done()
