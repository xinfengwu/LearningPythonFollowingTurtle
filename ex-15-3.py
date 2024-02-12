#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

for i in range(200):
    if i % 2 == 0:
        color('red')
    else:
        color('green')
    forward(i)
    right(91)
done()
