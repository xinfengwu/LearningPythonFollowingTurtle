#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
for i in range(100):
    pendown()
    setheading(i * 3.6)  # 面向i*3.6度
    forward(150)
    penup()
    backward(150)
done()
