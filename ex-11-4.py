#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle库

shape('turtle')  # 显示海龟图标
speed(10)  # 快速绘制
m = 2
# 外层循环，绘制3个旋转等边三角形
for i in range(20):
    # 内层循环，绘制一个正方形
    for j in range(4):
        forward(m)
        right(90)
    m = i + m
done()  # 绘制结束
