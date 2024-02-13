#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
speed(0)
colors = ['red', 'green', 'blue']
left(15)
for i in range(30):
    color(colors[i % 3])
    forward(200)
    backward(250)
    forward(50)
    left(150 / 30)
done()
