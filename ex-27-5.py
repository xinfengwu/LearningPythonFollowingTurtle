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


R = 360  # 大圆半径
r = R / 3  # 小圆半径
drawArc(0, 0, R, 0, 180)
drawArc(-2 * r, 0, r, 0, 180)
drawArc(0, 0, r, 0, 180)
drawArc(2 * r, 0, r, 0, 180)
penup()
goto(0, r)
setheading(270)
pendown()
forward(r + R)
drawArc(-10, -R, 10, 180, 360)
hideturtle()
done()
