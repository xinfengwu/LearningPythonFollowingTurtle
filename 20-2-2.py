#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
speed(0)
left(15)
for i in range(30):
    forward(200)
    backward(200)
    left(150 / 30)
done()
