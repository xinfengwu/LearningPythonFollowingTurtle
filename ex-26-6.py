#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
for r in range(101, 10, -10):
    if ((r // 10) % 2 == 0):
        color('red')
    else:
        color('white')
    begin_fill()
    circle(r)  # 绘制半径为100的空心圆
    end_fill()
done()
