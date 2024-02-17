#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义函数绘制空心圆（圆心坐标、半径、画笔粗细、画笔颜色）
def drawCircle(x, y, r, s, col):
    pensize(s)  # 设置画笔粗细为s
    color(col, 'white')  # 设置画笔颜色为col
    penup()
    #  home()  # 返回原点，面朝右边
    # 思路二range
    goto(x, y - r)
    pendown()
    begin_fill()
    circle(r)  # 在当前位置绘制半径为r的空心圆
    end_fill()
    penup()


# 定义函数，绘制同心圆(圆心坐标，最外层圆的半径，画笔粗细，画笔颜色，同心圆个数)
def drawConcentricCircles(x, y, R, s, col, n):
    for i in range(n):
        r = R - i * R / n
        drawCircle(x, y, r, s, col)


R = 40  # 外层同心圆的半径
setup(width=16 * R, height=16 * R)
hideturtle()
tracer(False)

for centerY in range(8 * R, -8 * R - 1, -R):
    for centerX in range(8 * R, -8 * R - 1, -2 * R):
        if (centerY / R) % 2 == 0:
            offset = R
        else:
            offset = 0
        drawConcentricCircles(centerX + offset, centerY, R, 1, 'black', 10)
done()
