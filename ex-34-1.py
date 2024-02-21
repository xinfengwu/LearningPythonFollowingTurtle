#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
from datetime import datetime  # 导入日期时间库
import time


def drawBackground(x, y, R):
    # 绘制空心圆
    penup()
    color('black')
    pensize(2)
    goto(x, y - R)
    pendown()
    circle(R)  # ? 运行时有bug
    penup()
    # 绘制刻度
    for angle in range(0, 360, 6):
        len_scale = R / 10  # 刻度长度
        goto(x, y)
        setheading(angle)
        if angle % 90 == 0:  # 画12点、3点、6点、9点钟刻度
            pensize(4)
            color('red')
            len_scale = R / 10
        elif angle in [30, 60, 120, 150, 210, 240]:  # 画1、2、4、5、7、8、10、11点钟刻度
            pensize(4)
            color('black')
            len_scale = R / 12
        else:  # 画其他刻度
            pensize(2)
            color('black')
            len_scale = R / 15
        forward(R - len_scale)
        pendown()
        forward(len_scale)
        penup()
        


# 针类
class Needle:
    def __init__(self, x, y, angle, ps, pc, length):
        self.x = x
        self.y = y
        self.angle = angle  # 针的角度
        self.ps = ps  # 针粗细
        self.pc = pc  # 针颜色
        self.length = length  # 针长度

    def draw(self):
        penup()
        goto(self.x, self.y)
        setheading(self.angle)
        color(self.pc)
        pensize(self.ps)
        pendown()
        forward(self.length)

    def update(self, angle):
        self.angle = angle


R = 200  # 空心圆半径
td = datetime.today()  # 获得今天的时间
second = td.second  # 获得当前秒
minute = td.minute  # 获得当前分
hour = td.hour  # 获得当前时
second_angle = -second * 6 + 90
minute_angle = -minute * 6 + 90
hour_angle = -hour % 12 * 30 + 90 - 30 / 60 * minute
hideturtle()
#  tracer(False)
hourNeedle = Needle(0, 0, hour_angle, 8, 'red', 2 * R / 5)
minuteNeedle = Needle(0, 0, minute_angle, 4, 'green', 3 * R / 5)
secondNeedle = Needle(0, 0, second_angle, 2, 'purple', 4 * R / 5)
while True:
    tracer(False)
    clear()
    td = datetime.today()  # 获得今天的时间
    second = td.second  # 获得当前秒
    minute = td.minute  # 获得当前分
    hour = td.hour  # 获得当前时
    # 设置时分秒针的角度
    second_angle = -second * 6 + 90
    minute_angle = -minute * 6 + 90
    hour_angle = -hour % 12 * 30 + 90 - 30 / 60 * minute
    # 绘制时分秒针
    hourNeedle.draw()
    minuteNeedle.draw()
    secondNeedle.draw()
    #更新时分秒针的角度
    hourNeedle.update(hour_angle)
    minuteNeedle.update(minute_angle)
    secondNeedle.update(second_angle)
    # 绘制背景
    drawBackground(0, 0, R)
    tracer(True)

