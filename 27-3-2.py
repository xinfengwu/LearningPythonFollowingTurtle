#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')


# 定义函数,画填充半圆（圆心坐标，半径，颜色）
def drawArc(x, y, r, col):
    color(col)
    penup()
    goto(x, y)  # 移动到圆心坐标
    setheading(0)  # 设置小海龟起始朝向
    forward(r)  # 前进距离r
    left(90)  # 左转90度
    pendown()
    begin_fill()
    circle(r, 180)  # 绘制半圆弧
    goto(x + r, y)  # 移动到圆心坐标
    end_fill()


# 画🌈彩虹
colors = [
    'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'white'
]
for i in range(0, 8):
    r = 250 - i * 15  # 从大到小的半径
    drawArc(0, 0, r, colors[i])
hideturtle()
done()
