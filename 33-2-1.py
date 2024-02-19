#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
import time  # 导入时间处理模块

h = 400  # 窗口高度
w = 600  # 窗口宽度


class Ball:  # 小球类
    x = 0
    y = 0
    d = 50
    vy = 3  # 小球y方向速度
    vx = 4  # 小球x方向速度


ball = Ball()


# 定义绘制填充圆函数（x、y坐标、直径）
def draw():
    penup()
    goto(ball.x, ball.y)
    pendown()
    dot(ball.d, 'red')


# 更新函数
def update():
    # 碰到左右边界，小球速度反向
    if ball.x <= (-w / 2 + ball.d / 2) or ball.x >= (w / 2 - ball.d / 2):
        ball.vx = -ball.vx
    # 碰到上下边界，小球速度反向
    if ball.y <= (-h / 2 + ball.d / 2) or ball.y >= (h / 2 - ball.d / 2):
        ball.vy = -ball.vy
    # 根据速度更新小球坐标
    ball.x = ball.x + ball.vx  # x坐标受速度影响变化
    ball.y = ball.y + ball.vy  # y坐标受速度影响变化


setup(width=w, height=h)
hideturtle()
while True:
    tracer(False)
    clear()  # 清空屏幕
    draw()
    update()
    tracer(True)  # 显示绘制过程
    time.sleep(0.01)  # 暂停0.01毫秒
done()
