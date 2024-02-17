#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')


# 定义函数绘制空心圆弧（圆心坐标，半径，起止角度）
def drawArc(x, y, r, a1, a2):
    penup()
    goto(x, y)  # 移动到圆心坐标
    setheading(a1)  # 设置小海龟起始朝向
    forward(r)  # 前进距离r
    left(90)  # 左转90度
    pendown()
    circle(r, a2 - a1)  # 在左侧绘制角度a2-a1的圆弧


drawArc(0, 0, 100, 0, 180)
drawArc(100, 100, 100, 90, 270)
drawArc(0, 200, 100, 180, 360)
drawArc(-100, 100, 100, 270, 450)
hideturtle()
done()
