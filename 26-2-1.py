#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

for i in range(10):  # 绘制10条平行线
    pensize(i)  # 设置画笔粗细为i
    penup()
    goto(0, i * 25)  # 移动到起始位置
    pendown()
    goto(250, i * 25)  # 移动到终止位置
hideturtle()
done()
