#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

for d in range(400, 0, -50):
    i = d // 50
    if i % 2 == 0:
        color('black')
    else:
        color('yellow')
    dot(d)
done()
