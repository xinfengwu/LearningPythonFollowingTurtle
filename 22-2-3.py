#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

for d in range(400, 0, -100):
    color('black')
    dot(d)
    color('yellow')
    dot(d - 50)
done()
