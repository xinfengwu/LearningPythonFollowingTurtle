#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
import time  # 导入时间处理模块
import random

h = 400  # 窗口高度
w = 600  # 窗口宽度


class Ball:  # 小球类
    # 使用构造函数传递参数对对象初始化
    def __init__(self, x, y, vx, vy, d, col):
        self.x = x
        self.y = y
        self.vx = vx  # 小球x方向速度
        self.vy = vy  # 小球y方向速度
        self.d = d
        self.col = col

    # 定义绘制填充圆函数（x、y坐标、直径）
    def draw(self):
        penup()
        goto(self.x, self.y)
        pendown()
        dot(self.d, self.col)

    # 更新函数
    def update(self):
        # 碰到左右边界，小球速度反向
        if self.x <= (-w / 2 + self.d / 2) or self.x >= (w / 2 - self.d / 2):
            self.vx = -self.vx
        # 碰到上下边界，小球速度反向
        if self.y <= (-h / 2 + self.d / 2) or self.y >= (h / 2 - self.d / 2):
            self.vy = -self.vy
        # 根据速度更新小球坐标
        self.x = self.x + self.vx  # x坐标受速度影响变化
        self.y = self.y + self.vy  # y坐标受速度影响变化


setup(width=w, height=h)
hideturtle()
balls = []
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']


# 添加一个小球
def addBall(x, y):
    d = random.randint(20, 60)  # 小球直径
    vy = random.randint(2, 6)  # 小球y方向速度
    vx = random.randint(1, 4)  # 小球x方向速度
    col = random.choice(colors)
    ball = Ball(x, y, vx, vy, d, col)
    balls.append(ball)


onscreenclick(addBall(x, y))
while True:
    tracer(False)
    clear()  # 清空屏幕
    for ball in balls:
        ball.draw()
        ball.update()
    tracer(True)  # 显示绘制过程
    time.sleep(0.01)  # 暂停0.01毫秒
done()
