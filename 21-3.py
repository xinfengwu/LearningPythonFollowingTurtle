#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

speed(0)
colors = [
    'red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black'
]
for i in range(230):
    color(colors[i % 8])
    penup()
    forward(i + i / 2)
    offset = -1
    angle = 360 / 8 + offset
    right(angle)
    pendown()
    for j in range(6):
        forward(i / 8)
        right(60)
done()
