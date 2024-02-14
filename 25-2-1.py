#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义绘制填充正方形函数（左上角x、y坐标、边长、颜色）
def drawSquare(x, y, l, col):
    color(col)
    penup()
    goto(x, y)  # 移动到目标位置
    pendown()
    begin_fill()  # 开始填充
    for i in range(4):
        forward(l)
        right(90)
    end_fill()  # 结束填充


bgcolor('yellow')  # 设置背景颜色
drawSquare(0, 0, 100, 'black')
drawSquare(100, 0, 100, 'white')
hideturtle()
done()
