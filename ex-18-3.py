#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
# speed(0)
colors = ['pink', 'yellow', 'green', 'blue', 'purple', 'red']
for i in range(150):
    index = i % 6
    color(colors[index])
    forward(i)
    right(60)
hideturtle()
done()
