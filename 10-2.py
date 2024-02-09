#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
n = int(input('请输入正多边形的边数： '))
speed(0)
offset = float(input('请输入偏移的角度值： '))
angle = 360 / n + offset
for i in range(200):
    forward(i)
    right(angle)
done()
