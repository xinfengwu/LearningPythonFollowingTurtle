#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
for i in range(4):
    if i % 2 == 0:
        color('red')
    else:
        color('green')
    forward(150)
    right(90)
done()
