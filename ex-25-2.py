#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

goto(0, 0)
dot(320, 'red')
penup()
goto(-100, 25)
color('white')
begin_fill()
for i in range(2):
    forward(200)
    right(90)
    forward(50)
    right(90)
end_fill()
hideturtle()
done()
