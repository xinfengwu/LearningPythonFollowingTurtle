#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')

step = 100
for i in range(step):
    color('black')
    circle(100, 180 / step)
    color('white')
    circle(100, 180 / step)
hideturtle()
done()
