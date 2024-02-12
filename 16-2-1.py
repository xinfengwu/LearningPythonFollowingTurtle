#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle

speed(0)  # 快速绘制
# 计算螺旋线的角度：边数为3,偏移角度0.8
angle = 360 / 3 + 0.8
for i in range(225):
    if i % 3 == 0:  # 红色
        color('red')
    if i % 3 == 1:  # 绿色
        color('green')
    if i % 3 == 2:  # 蓝色
        color('blue')
    forward(2 * i)  # 前进
    right(angle)  # 右转
done()  # 绘制结束
