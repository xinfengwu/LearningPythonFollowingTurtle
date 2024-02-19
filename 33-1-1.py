#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
import time  # 导入时间处理模块

h = 400  # 窗口高度
w = 600  # 窗口宽度
setup(width=w, height=h)
hideturtle()
x = 0
y = 0
d = 50
vy = 3  # 小球y方向速度
vx = 4  # 小球x方向速度
ball = [x, y, vx, vy, d]


# 定义绘制填充圆函数（x、y坐标、直径）
def draw():
    penup()
    goto(ball[0], ball[1])
    pendown()
    dot(ball[4], 'red')


# 更新函数
def update():
    # 碰到左右边界，小球速度反向
    if ball[0] <= (-w / 2 + ball[4] / 2) or ball[0] >= (w / 2 - ball[4] / 2):
        ball[2] = -ball[2]
    # 碰到上下边界，小球速度反向
    if ball[1] <= (-h / 2 + ball[4] / 2) or ball[1] >= (h / 2 - ball[4] / 2):
        ball[3] = -ball[3]
    # 根据速度更新小球坐标
    ball[0] = ball[0] + ball[2]  # x坐标受速度影响变化
    ball[1] = ball[1] + ball[3]  # y坐标受速度影响变化


while True:
    tracer(False)
    clear()  # 清空屏幕
    draw()
    update()
    tracer(True)  # 显示绘制过程
    time.sleep(0.01)  # 暂停0.01毫秒
done()
