#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle
import time
import random

h = 600  # 窗口高度
w = 800  # 窗口宽度
turtle.setup(width=w, height=h)  # 设置绘图窗口大小
birdImage = 'bird.gif'
turtle.addshape(birdImage)
g = -0.3  # 重力加速度
pipeNum = 4  # 水管障碍物的个数


class Bird:  # 小鸟类
    def initialize(self):  # 成员函数，对象初始化
        self.x = -w / 3
        self.y = h / 3
        self.d = 50  # 小鸟直径
        self.vy = 0  # 小鸟y方向的速度
        self.score = 0  # 得分初始为0

    def draw(self):  # 成员函数，绘制小鸟和得分
        # 输出当前得分
        turtle.penup()
        turtle.goto(-350, 220)
        turtle.color('red')
        turtle.write(str(self.score), align='center', font=('宋体', 28))
        # 绘制小鸟
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.shape(birdImage)
        turtle.showturtle()

    def update(self):  # 更新小鸟
        # 根据重力加速度更新小鸟速度
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
        self.xLeft = w / 2  # 开始水管在画面右端
        self.xRight = w / 2 + self.width
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
            #  self.initialize()
            b.score = 0  # 得分设为0


bird = Bird()  # 创建小鸟对象
bird.initialize()
turtle.onscreenclick(bird.flyUp)  # 单击鼠标左键，小鸟向上飞
pipes = []  # 水管列表
for i in range(pipeNum):
    # 创建水管对象
    pipe = Pipe()
    # 水管对象初始化
    pipe.initialize()
    # 水平平均分布水管的水平位置
    pipe.xLeft += i * (w + pipe.width) / pipeNum
    pipe.xRight = pipe.xLeft + pipe.width
    pipes.append(pipe)  # 添加pipe 到水管列表中

while True:  # 循环重复执行
    turtle.tracer(False)
    turtle.clear()
    turtle.bgpic('background.gif')
    for pipe in pipes:  # 绘制所有水管
        pipe.draw()
    bird.draw()  # 绘制小鸟
    turtle.tracer(True)
    for pipe in pipes:  # 更新所有水管状态
        pipe.update(bird)
    bird.update()  # 更新小鸟
    time.sleep(0.01)
#  done()
