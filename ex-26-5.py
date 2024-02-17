#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义函数绘制线段（起点x坐标、起点y坐标、终点x坐标、终点y坐标、颜色、画笔粗细）
def drawLine(x1, y1, x2, y2, col='white', ps=5):
    pensize(ps)
    color(col)
    goto(x1, y1)
    pendown()
    goto(x2, y2)
    penup()


# 定义函数绘制点（x坐标、y坐标、直径、颜色）
def drawDot(x, y, d, col):
    penup()
    color(col)
    goto(x, y)
    pendown()
    dot(d)
    penup()


speed(0)
bgcolor('black')
step = 50
# 画网格
for i in range(0, 250, step):
    drawLine(x1=0, y1=i, x2=6 * step, y2=i, col='gray')  # 水平线
    drawLine(x1=i + step, y1=-step, x2=i + step, y2=5 * step,
             col='gray')  # 垂直线
# 画白点
for i in range(0, 250, step):
    for j in range(0, 250, step):
        drawDot(x=i + step, y=j, d=10, col='white')

hideturtle()
done()
