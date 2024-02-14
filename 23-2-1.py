#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

for i in range(5):
    penup()
    goto(0, i * 50)  # 移动到线段起始位置
    pendown()
    goto(250, i * 50)  # 移动到线段终止位置
hideturtle()
done()
