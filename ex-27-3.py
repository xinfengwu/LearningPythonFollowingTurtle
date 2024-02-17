#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义函数绘制空心圆（圆心坐标、半径、画笔粗细、画笔颜色）
def drawCircle(x, y, r, s, col):
    pensize(s)  # 设置画笔粗细为s
    color(col)  # 设置画笔颜色为col
    penup()
    #  home()  # 返回原点，面朝右边
    # 思路二
    goto(x, y - r)
    pendown()
    circle(r)  # 在当前位置绘制半径为r的空心圆
    penup()


# 定义函数画云纹(最外层线段长度、画笔粗细、画笔颜色)
def drawClodpattern(l, s, col):
    pensize(s)  # 设置画笔粗细为s
    color(col)  # 设置画笔颜色为col
    pendown()
    for i in range(6):
        forward(l - i * l / 6)
        left(91)
    penup()


shape('turtle')

speed(0)
# 画大空心圆
drawCircle(0, 0, 200, 5, 'black')
# 画小空心圆
drawCircle(0, 0, 150, 5, 'black')
# 画云纹
n = 20  # 云纹个数
for i in range(n):
    home()
    setheading(i * 360 / n)
    penup()
    forward(150)
    pendown()
    drawClodpattern(40, 5, 'black')
hideturtle()
done()
