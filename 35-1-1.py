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


class Bird:  # 小鸟类
    def initialize(self):  # 成员函数，对象初始化
        self.x = -w / 3
        self.y = h / 3
        self.d = 50  # 小球直径

    def draw(self):  # 成员函数，绘制小鸟
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color('white')
        turtle.dot(self.d)


bird = Bird()  # 创建小鸟对象
bird.initialize()
while True:  # 循环重复执行
    turtle.tracer(False)
    turtle.clear()
    bird.draw()
    turtle.tracer(True)
    time.sleep(0.01)
done()
