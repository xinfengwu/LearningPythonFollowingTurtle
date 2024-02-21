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
        self.vy = 0  # 小球y方向的速度
        self.score = 0  # 得分初始为0

    def draw(self):  # 成员函数，绘制小鸟
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color('white')
        turtle.dot(self.d)
        # 输出当前得分
        turtle.penup()
        turtle.goto(-350, 220)
        turtle.color('red')
        turtle.write(str(self.score), align='center', font=('宋体', 28))

    def update(self):  # 更新小鸟
        # 根据重力加速度更新小球速度
        self.vy = self.vy + g
        # 根据速度更新y坐标
        self.y = self.y + self.vy
        # 碰到下边界时，小鸟状态重置
        if self.y <= -h / 2 + self.d / 2:
            self.initialize()

    # 小鸟向上飞
    def flyUp(self, x, y):
        self.vy = 10  # 速度向上


class Pipe:  # 水管
    def initialize(self):
        self.width = 40
        self.gapHeight = h / 2  # 中间空隙高度为画面高度一半
        self.xLeft = w / 3  # 开始水管干在画面右端
        self.xRight = w / 3 + self.width
        # 设定随机空隙上、下位置
        self.yGapTop = random.randint(20, h / 2 - 20)
        self.yGapBottom = self.yGapTop - self.gapHeight
        self.vx = -3  # 向左运动的速度

    def draw(self):
        turtle.color('yellow')
        # 绘制上部水管填充矩形
        turtle.penup()
        turtle.goto(self.xLeft, h / 2)  # 移动到坐标位置
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(self.xRight, h / 2)
        turtle.goto(self.xRight, self.yGapTop)
        turtle.goto(self.xLeft, self.yGapTop)
        turtle.end_fill()
        # 绘制下部水管填充矩形
        turtle.penup()
        turtle.goto(self.xLeft, self.yGapBottom)  # 移动到坐标位置
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(self.xRight, self.yGapBottom)
        turtle.goto(self.xRight, -h / 2)
        turtle.goto(self.xLeft, -h / 2)
        turtle.end_fill()

    def update(self, b):
        if self.xRight < -w / 2:  # 如果到达最右边
            self.initialize()  # 初始化，在右边重新出现
            b.score += 1  # 得分加1
        self.xLeft = self.xLeft + self.vx  # 水管逐渐向左移动
        self.xRight = self.xLeft + self.width
        # 碰撞检测
        if b.x + b.d / 2 > self.xLeft and b.x - b.d / 2 < self.xRight and (
                b.y + b.d / 2 > self.yGapTop
                or b.y - b.d / 2 < self.yGapBottom):
            self.initialize()
            b.score = 0  # 得分设为0


bird = Bird()  # 创建小鸟对象
bird.initialize()
turtle.onscreenclick(bird.flyUp)
pipe = Pipe()
pipe.initialize()
while True:  # 循环重复执行
    turtle.tracer(False)
    turtle.clear()
    bird.draw()
    pipe.draw()
    bird.update()
    pipe.update(bird)
    turtle.tracer(True)
    time.sleep(0.01)
done()
