#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')


# 定义函数绘制封闭圆弧（圆心坐标，半径，起止角度）
def drawArc(x, y, r, a1, a2):
    penup()
    goto(x, y)  # 移动到圆心坐标
    setheading(a1)  # 设置小海龟起始朝向
    pendown()
    forward(r)  # 前进距离r
    left(90)  # 左转90度
    pendown()
    circle(r, a2 - a1)  # 在左侧绘制角度a2-a1的圆弧
    left(90)  # 左转90度
    goto(x, y)  # 移动到圆心坐标


drawArc(0, 0, 100, 0, 180)
done()
