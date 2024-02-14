#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义绘制线段函数，参数为起始、终止点坐标
def line(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)


speed(4)
color('black')
step = 55  # 折线间距
width = 300  # 图形直径
height = 200  # 图形高度
# 画黑林
for i in range(12):  # 画12条折线
    line(0, height, -(width - i * step), height / 2)  # 画上折线
    line(-(width - i * step), height / 2, 0, 0)  # 画下折线
# 画两条红色平行线
color('red')
line(-width, 3 * height / 4, width, 3 * height / 4)  # 画上红线
line(-width, height / 4, width, height / 4)  # 画下红线
hideturtle()
done()
