#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

shape('turtle')
for i in range(4):
    pendown()
    setheading(i * 90)
    forward(150)
done()
