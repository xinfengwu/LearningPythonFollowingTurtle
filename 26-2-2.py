#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')


# 定义函数绘制空心圆（圆心坐标、半径、画笔粗细、颜色）
def drawCircle(x, y, r, s, col):
    pensize(s)  # 设置画笔粗细为s
    color(col)  # 设置画笔颜色为col
    penup()
    home()  # 返回原点，面朝右边
    # 思路二
    goto(x, y - r)
    pendown()
    circle(r)  # 在当前位置绘制半径为r的空心圆


drawCircle(100, 100, 50, 5, 'red')
done()
