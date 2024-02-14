#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义绘制线段函数，参数为起始、终止点坐标
def line(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)


speed(0)
step = 15
for i in range(19):
    line(0, i * step, 18 * step, i * step)  # 绘制水平线
    line(i * step, 0, i * step, 18 * step)  # 绘制垂直线
hideturtle()
done()
