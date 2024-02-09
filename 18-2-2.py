#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
speed(0)
colors = ['red', 'green', 'blue', 'yellow']
for i in range(150):
    index = i % 4
    color(colors[index])
    forward(i)
    right(91)
hideturtle()
done()
