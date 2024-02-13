#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

speed(0)
shape('turtle')
# 方法一：
#  for i in range(5):
#  forward(50)
#  left(90)
#  forward(50)
#  right(90)
#  forward(50)
#  right(90)
#  forward(50)
#  left(90)
#  forward(50)
# 方法二：
for i in range(5):
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    forward(-50)
done()
