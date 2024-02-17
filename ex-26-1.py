#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')


# 定义函数绘制空心圆（圆心坐标、半径）
def drawCircle(x, y, r):
    penup()
    home()  # 返回原点，面朝右边
    # 思路二
    goto(x, y - r)
    pendown()
    circle(r)  # 在当前位置绘制半径为r的空心圆


color('pink')
begin_fill()
drawCircle(100, 100, 50)
end_fill()
colors = [
    'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'pink',
    'brown', 'black'
]
for i in range(10):
    color(colors[i])
    penup()
    goto(100, 100)
    penup()
    forward(50 + 10)
    pendown()
    forward(100)
    right(36)
done()
