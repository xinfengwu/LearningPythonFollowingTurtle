#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle库

begin_fill()  # 开始填充
penup()
for i in range(4):
    forward(100)
    right(90)

end_fill()  # 结束填充
hideturtle()
done()
