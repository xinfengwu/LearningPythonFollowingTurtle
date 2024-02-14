#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

# 画鱼眼
color('black')
goto(0, 0)
pendown()
dot(10)
# 画身体
color('red')
penup()
goto(-50, 0)
pendown()
goto(100, 100)
goto(100, -100)
goto(-50, 0)
# 画鱼尾
color('orange')
penup()
goto(100, 0)
pendown()
goto(150, 50)
goto(150, -50)
goto(100, 0)
done()
