#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
import time  # 导入时间处理模块

h = 400  # 窗口高度
w = 600  # 窗口宽度
step = 40  # 条纹间距
setup(width=w, height=h)
hideturtle()
tracer(False)
# 绘制背景
bgcolor('white')
for x in range(-int(w / 2), int(w / 2 + 1), step):
    penup()
    goto(x, h / 2)
    pendown()
    color('black')
    begin_fill()
    for i in range(2):
        forward(step / 2)
        right(90)
        forward(h)
        right(90)
    end_fill()
x = 0
y = 0
d = 50
vx = -3  # 小球x方向速度


# 定义函数,绘制方块（x、y坐标、颜色）
def draw():
    penup()
    goto(x - 1.5 * step, y)
    pendown()
    color('blue')
    begin_fill()
    for i in range(2):
        forward(3 * step)
        right(90)
        forward(step)
        right(90)
    end_fill()
    penup()
    goto(x - 1.5 * step, y - 2 * step)
    pendown()
    color('yellow')
    begin_fill()
    for i in range(2):
        forward(3 * step)
        right(90)
        forward(step)
        right(90)
    end_fill()


# 更新函数
def update():
    global x, vx, y, vy
    # 碰到左右边界，小球速度反向
    if x <= (-w / 2 + 3 * step / 2) or x >= (w / 2 - 3 * step / 2):
        vx = -vx
    # 根据速度更新小球坐标
    x = x + vx  # x坐标受速度影响变化


while True:
    tracer(False)
    clear()  # 清空屏幕
    draw()
    update()
    tracer(True)  # 显示绘制过程
    time.sleep(0.01)  # 暂停0.01毫秒
done()
