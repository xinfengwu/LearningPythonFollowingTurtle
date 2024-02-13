#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

n = 40
offset = 0.1
angle = 360 / n + offset
for i in range(300):
    pendown()
    forward(i / n)
    penup()
    forward(i / n)
    right(angle)
done()
