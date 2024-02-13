#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle库

speed(0)  # 快速绘制
# 以下循环绘制四色螺旋曲线
for i in range(150):
    if i % 4 == 0:  # i除以4余0
        color('red')  # 设为红色
    elif i % 4 == 1:  # i除以4余1
        color('green')  # 设为绿色
    elif i % 4 == 2:  # i除以4余2
        color('blue')  # 设为蓝色
    else:  # i除以4余3
        color('yellow')  # 设为黄色
    forward(i)  # 前进
    right(91)  # 右转
done()  # 结束绘制
