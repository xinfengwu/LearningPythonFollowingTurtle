#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义绘制线段函数，参数为起始、终止点坐标
def line(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)


line(0, 0, 300, 200)
hideturtle()
done()
