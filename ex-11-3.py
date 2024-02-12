#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle库

shape('turtle')  # 显示海龟图标
speed(10)  # 快速绘制
# 外层循环，绘制3个旋转等边三角形
for i in range(6):
    # 内层循环，绘制一个等边三角形
    for j in range(3):
        forward(100)
        right(120)
    right(360 / 6)  # 绘制右转
done()  # 绘制结束
