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
R = 40  # 基础单元外围黑白圆弧半径
step = 2.5 * R  # 两个基础单元圆心距离
for j in range(-2, 3):  # 对行进行遍历
    for i in range(-3, 4):  # 对列进行遍历
        centerY = j * step  # 当前圆心y坐标
        centerX = i * step  # 当前圆心x坐标
        angle = 45 * ((i + j) % 6)  # 黑色圆半弧的起始角度
        drawUnit(centerX, centerY, R, angle)  # 绘制基础单元
hideturtle()
done()
