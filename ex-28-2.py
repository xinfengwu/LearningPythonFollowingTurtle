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
    i = 5  # 黑或白圆弧的度数
    drawPie(x, y, r, angle, angle + i, 'white')
    drawPie(x, y, r, angle + i, angle + 3 * i, 'cyan')  # 白色圆弧的2倍
    drawPie(x, y, r, angle + 3 * i, angle + 4 * i, 'black')
    drawPie(x, y, r, angle + 4 * i, angle + 6 * i, 'red')


# 定义函数，绘制一组同心圆(起始角度，偏移角度)
def drawGroupCirle(x, y, angle, offset):
    for R in range(100, 39, -20):  # 遍历4个同心圆的半径
        for i in range(0, 360, 30):
            drawUnit(x, y, R, angle + i)
        angle = angle + offset  # 下一个同心圆的起始角度


setup(width=1200, height=1200)  # 设置窗口大小
tracer(False)
#  speed(9)
bgcolor('grey')
for centerX in range(-200, 201, 200):
    for centerY in range(-100, 201, 200):
        drawGroupCirle(centerX, centerY, 0, 15)  # 绘制一组同心圆
hideturtle()
done()
