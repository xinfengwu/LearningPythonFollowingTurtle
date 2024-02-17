#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')


# 定义函数绘制空心圆（圆心坐标、半径）
def drawCircle(x, y, r):
    penup()
    home()  # 返回原点，面朝右边
    goto(x, y - r)
    pendown()
    circle(r)  # 在当前位置绘制半径为r的空心圆


for r in range(10, 101, 10):
    drawCircle(0, 0, r)
done()
