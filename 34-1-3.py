#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
import time


# 定义函数，绘制圆盘等游戏背景图形
def drawBackground():
    #绘制画面中间的红色空心圆盘
    penup()
    goto(0, -50)
    setheading(0)
    pendown()
    color('red')
    circle(50)


class Needle:  #针类
    angle = 180  # 针的角度

    def draw(self):
        color('purple')
        pensize(2)
        penup()
        goto(0, 0)
        setheading(self.angle)
        pendown()
        forward(150)

    def update(self):
        # 角度不断增加
        self.angle = self.angle + 1


hideturtle()
setup(width=600, height=400)
needles = []
for a in range(0, 360, 10):
    newNeedle = Needle()  # 新建一根针
    newNeedle.angle = a  # 设定新针的角度
    needles.append(newNeedle)  # 把新增添加到针列表中
while True:
    tracer(False)
    clear()
    for needle in needles:
        needle.update()
        needle.draw()
    drawBackground()
    tracer(True)
    time.sleep(0.01)
done()
