#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
n = int(input('请输入正多边形的边数： '))
angle = 360 / n
for i in range(n):
    forward(100)
    right(angle)
done()
