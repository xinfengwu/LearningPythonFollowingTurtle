#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle库

# 画橙色五角星
color('orange', 'purple')  # 设为画笔线条颜色为橙色,填充颜色为紫色
for i in range(5):
    forward(120)
    right(144)

penup()
forward(200)

# 画紫色五角星(有交叉线）
pendown()
begin_fill()  # 开始填充
for i in range(5):
    forward(120)
    right(144)

end_fill()  # 结束填充

penup()
forward(200)
# 画紫色五角星（无交叉线)
pendown()
begin_fill()  # 开始填充
for i in range(5):
    forward(38)
    right(144)
    forward(38)
    right(-72)
end_fill()  # 结束填充

hideturtle()
done()
