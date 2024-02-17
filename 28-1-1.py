#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')


# 定义函数,绘制填充扇形（圆心坐标，半径，起止角度,颜色）
def drawPie(x, y, r, a1, a2, col):
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


# 定义函数，画基本单元（圆心坐标，半径，起始角度）
def drawUnit(x, y, r, angle):
    drawPie(x, y, r, angle, angle + 180, 'black')
    drawPie(x, y, r, angle + 180, angle + 360, 'white')
    drawPie(x, y, r * 0.9, 0, 360, 'blueviolet')


speed(0)
bgcolor('orange')
# 画一个基础单元：圆心：（0,0)、半径100、起始45度
drawUnit(0, 0, 100, 45)
hideturtle()
done()
