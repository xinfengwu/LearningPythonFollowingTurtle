#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle
import time
import random

h = 600  # 窗口高度
w = 800  # 窗口宽度
turtle.setup(width=w, height=h)  # 设置绘图窗口大小
turtle.bgcolor('black')  # 背景黑色
turtle.hideturtle()
g = -0.3  # 重力加速度


class Bird:  # 小鸟类
    def initialize(self):  # 成员函数，对象初始化
        self.x = -w / 3
        self.y = h / 3
        self.d = 50  # 小球直径
        self.vy = 0  #小球y方向的速度

    def draw(self):  # 成员函数，绘制小鸟
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color('white')
        turtle.dot(self.d)

    def update(self):  #更新小鸟
        # 根据重力加速度更新小球速度
        self.vy = self.vy + g
        # 根据速度更新y坐标
        self.y = self.y + self.vy
        # 碰到下边界时，小鸟状态重置
        if self.y <= -h / 2 + self.d / 2:
            self.initialize()


bird = Bird()  # 创建小鸟对象
bird.initialize()
while True:  # 循环重复执行
    turtle.tracer(False)
    turtle.clear()
    bird.draw()
    bird.update()
    turtle.tracer(True)
    time.sleep(0.01)
done()
