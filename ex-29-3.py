#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义函数绘制空心圆（圆心坐标，半径）
def drawCircle(x, y, r):
    penup()
    setheading(0)
    goto(x, y - r)
    pendown()
    circle(r)


# 定义函数绘制圆组（圆心坐标，半径）
def drawCircles(x, y, radius):
    drawCircle(x, y, radius)  # 绘制中间大圆
    if radius > 10:
        drawCircles(x - 1.5 * radius, y, 0.5 * radius)  # 绘制左边小圆
        drawCircles(x + 1.5 * radius, y, 0.5 * radius)  # 绘制右边小圆
        drawCircles(x, y - 1.5 * radius, 0.5 * radius)  # 绘制上边小圆
        drawCircles(x, y + 1.5 * radius, 0.5 * radius)  # 绘制下边小圆


setup(width=600, height=600)
tracer(False)
drawCircles(0, 0, 100)
penup()
goto(-20, -150)
color('red')
write('福', align='center', font=('宋体', 200))
done()
