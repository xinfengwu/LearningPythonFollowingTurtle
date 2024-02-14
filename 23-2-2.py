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
hideturtle()
done()
