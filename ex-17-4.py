#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

colors = ['red', 'yellow', 'blue', 'cyan', 'purple', 'pink', 'orange']
for c in colors:
    color(c)
    for i in range(2):
        forward(200)
        right(90)
        forward(50)
        right(90)
    right(360 / 7)
done()
