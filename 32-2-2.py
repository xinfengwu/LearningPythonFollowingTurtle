#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
import time  # 导入时间处理模块

x = 0
y = 200
d = 50
vy = -3  # 小球y方向速度


# 定义绘制填充圆函数（x、y坐标、直径）
def draw():
    penup()
    goto(x, y)
    pendown()
    dot(d, 'red')


# 更新函数
def update():
    global y, vy
    y = y + vy  # y坐标受速度影响变化


hideturtle()
while True:
    tracer(False)
    clear()  # 清空屏幕
    draw()
    update()
    tracer(True)  # 显示绘制过程
    time.sleep(0.01)  # 暂停0.01毫秒
done()
