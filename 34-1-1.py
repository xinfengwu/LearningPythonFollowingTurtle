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


hideturtle()
setup(width=600, height=400)
needle = Needle()
while True:
    tracer(False)
    clear()
    needle.draw()
    drawBackground()
    tracer(True)
    time.sleep(0.01)
done()
