#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')


# 定义函数绘制空心圆（圆心坐标、半径、画笔粗细、颜色）
def drawCircle(x=0, y=0, radius=125, pen_size=10, pencolor='blue'):
    pensize(pen_size)  # 设置画笔粗细为s
    color(pencolor)  # 设置画笔颜色为col
    penup()
    home()  # 返回原点，面朝右边
    # 思路二
    goto(x, y - radius)
    pendown()
    circle(radius)  # 在当前位置绘制半径为r的空心圆


r = 125  # 每个圆的半径
h = 1.7 * r  # 上下两层圆心的垂直距离
xgap = 20  # 两圆之间的水平间距
drawCircle(x=-2 * r + (-xgap), y=-30, radius=r, pencolor='blue')
drawCircle(x=0, y=-30, radius=r, pencolor='black')  # 中心圆
drawCircle(x=2 * r + xgap, y=-30, radius=r, pencolor='red')
drawCircle(x=-(r + 0.5 * xgap), y=-h, radius=r, pencolor='yellow')
drawCircle(x=r + 0.5 * xgap, y=-h, radius=r, pencolor='green')
done()
