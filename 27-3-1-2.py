#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')


# 定义函数绘制实心圆弧（圆心坐标，半径，起止角度,颜色）
def drawArc(x, y, r, a1, a2, col):
    color(col)
    penup()
    goto(x, y)  # 移动到圆心坐标
    setheading(a1)  # 设置小海龟起始朝向
    begin_fill()
    pendown()
    forward(r)  # 前进距离r
    left(90)  # 左转90度
    pendown()
    circle(r, a2 - a1)  # 在左侧绘制角度a2-a1的圆弧
    left(90)  # 左转90度
    goto(x, y)  # 移动到圆心坐标
    end_fill()


# 画🌈彩虹
colors = [
    'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'white'
]
r = 100
for col in colors:
    r = r - 5
    drawArc(0, 0, r, 0, 180, col)
hideturtle()
done()
