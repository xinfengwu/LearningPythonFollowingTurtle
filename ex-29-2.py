#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义函数绘制实心圆（圆心坐标，半径）
def drawCircle(x, y, r):
    penup()
    setheading(0)
    goto(x, y - r)
    pendown()
    begin_fill()
    circle(r)
    end_fill()


# 定义函数绘制圆组（圆心坐标，半径）
def drawCircles(x, y, radius):
    drawCircle(x, y, radius)  # 绘制中间大圆
    if radius > 6:
        drawCircles(x - 3 * radius, y, 0.5 * radius)  # 绘制左边小圆
        drawCircles(x + 3 * radius, y, 0.5 * radius)  # 绘制右边小圆
        drawCircles(x, y + 3 * radius, 0.5 * radius)  # 绘制上边小圆
        drawCircles(x, y - 3 * radius, 0.5 * radius)  # 绘制下边小圆


tracer(False)
drawCircles(0, 0, 50)
done()
