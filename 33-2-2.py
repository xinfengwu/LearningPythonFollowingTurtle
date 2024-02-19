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

    # 定义绘制填充圆函数（x、y坐标、直径）
    def draw(self):
        penup()
        goto(self.x, self.y)
        pendown()
        dot(self.d, 'red')

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


ball = Ball()

setup(width=w, height=h)
hideturtle()
while True:
    tracer(False)
    clear()  # 清空屏幕
    ball.draw()
    ball.update()
    tracer(True)  # 显示绘制过程
    time.sleep(0.01)  # 暂停0.01毫秒
done()
