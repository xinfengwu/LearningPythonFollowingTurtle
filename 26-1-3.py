#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')


# 定义函数绘制空心圆（圆心坐标、半径）
def drawCircle(x, y, r):
    penup()
    home()  # 返回原点，面朝右边
    # 思路一
    #  goto(x, y)
    #  pendown()
    #  circle(y - r)  # 在当前位置绘制半径为y-r的空心圆
    # 思路二
    goto(x, y - r)
    pendown()
    circle(r)  # 在当前位置绘制半径为r的空心圆


drawCircle(100, 100, 50)
done()
