#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
import time
import random


# 定义函数，绘制圆盘等游戏背景图形
def drawBackground():
    #绘制画面中间的红色空心圆盘
    penup()
    goto(0, 0)
    pendown()
    color('red')
    #绘制实心圆
    dot(100)
    # 绘制左侧待发射区域的一根针
    penup()
    goto(-300, 0)
    color('purple')
    pensize(2)
    pendown()
    goto(-180, 0)


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
        self.angle = (self.angle + 1) % 360


# 鼠标点击后，增加一根针
def addNeedle(x, y):
    global gameOver  #全局变量
    if gameOver:  # 如果游戏结束状态，则函数直接返回
        return
    newNeedle = Needle()  # 新建一根针
    for needle in needles:  #对所有针遍历
        # 如果新增的角度和已有针角度接近
        if abs(needle.angle - newNeedle.angle) < 4:
            gameOver = True
            newNeedle.draw()  #绘制下新针
    needles.append(newNeedle)  # 把新增添加到针列表中


hideturtle()
setup(width=600, height=400)
needles = []
onscreenclick(addNeedle)
gameOver = False  # 初始不是游戏结束状态
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
