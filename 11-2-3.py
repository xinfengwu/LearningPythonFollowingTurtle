#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle库

shape('turtle')  # 显示海龟图标
speed(10)  # 快速绘制
n = int(input('请输入旋转正方形的个数： '))
# 外层循环，绘制6个旋转正方形
for i in range(n):
    # 内层循环，绘制一个正方形
    for j in range(4):
        forward(100)
        right(90)
    right(360 / n)  # 绘制一个正方形后右转
done()  # 绘制结束
