#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

speed(0)
step = 15  # 平行线间的距离
for i in range(19):  # 绘制19条水平平行线
    penup()
    goto(0, i * step)  # 移动到线段起始位置
    pendown()
    goto(18 * step, i * step)  # 移动到线段终止位置

for j in range(19):  # 绘制19条垂直平行线
    penup()
    goto(j * step, 0)  # 移动到线段起始位置
    pendown()
    goto(j * step, 18 * step)  # 移动到线段终止位置
for m in range(3):  # 绘制9个圆点
    for n in range(3):
        penup()
        color('black')
        goto(3 * step + m * 6 * step, 3 * step + n * 6 * step)
        pendown()
        dot(5)
hideturtle()
done()
