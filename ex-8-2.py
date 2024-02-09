#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
n = 100
angle = 360 / n
for i in range(n):
    forward(1)
    right(angle)
done()
