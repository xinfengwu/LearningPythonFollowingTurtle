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
    forward(i)
    right(44)
    pendown()
    for j in range(4):
        forward(5 + i / 8)
        right(90)
done()
