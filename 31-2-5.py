#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
import time  # 导入时间处理模块


# 定义绘制填充圆函数（x、y坐标、直径）
def drawCircle(x, y, d):
    penup()
    goto(x, y)
    pendown()
    dot(d, 'red')


speed(0)
hideturtle()
y = 200  # y坐标
while y >= -200:
    tracer(False)
    clear()  # 清空屏幕
    drawCircle(0, y, 50)
    tracer(True)  # 显示绘制过程
    time.sleep(0.01)  # 暂停0.01毫秒
    y -= 1
done()
