#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

speed(0)
bgcolor('cyan')
# 画底色
color('pink')
dot(100)
# 画螺旋线
color('white')
pensize(4)
n = 40
for i in range(170):
    forward(i / 20)
    right(360 / n + 0.1)
#  home()
# 画棒
penup()
goto(0, -50)
color('yellow')
pendown()
goto(0, -150)
done()
