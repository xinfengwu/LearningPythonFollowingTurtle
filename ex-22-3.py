#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

colors = [
    'white', 'purple', 'cyan', 'blue', 'green', 'yellow', 'orange', 'red'
]
for d in range(400, 0, -50):
    index = d // 50 - 1
    color(colors[index])
    dot(d)
done()
