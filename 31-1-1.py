#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义绘制填充圆函数（x、y坐标、直径）
def drawCircle(x, y, d):
    penup()
    goto(x, y)
    pendown()
    dot(d, 'red')


speed(0)
hideturtle()
for y in range(200, -201, -1):
    drawCircle(0, y, 50)
done()
