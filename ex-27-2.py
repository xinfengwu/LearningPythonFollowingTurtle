#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
n = int(input('请输入正多边形的边数： '))
for i in range(n):
    pendown()
    setheading(i * 360 / n)
    forward(150)
done()
