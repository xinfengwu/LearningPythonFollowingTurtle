#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

color('red')
d = 100
dot(d)
n = 12
angle = 360 / n
for i in range(n):
    right(angle)
    penup()
    forward(d * 2 / 3)
    pendown()
    forward(d / 3)
    penup()
    backward(d)
done()
