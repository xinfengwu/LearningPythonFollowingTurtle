#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle库

shape('turtle')  # 显示海龟图标
speed(10)  # 快速绘制
# 外层循环，绘制6个旋转长方形
for i in range(6):
    # 内层循环，绘制一个长方形
    for j in range(2):
        forward(100)
        right(90)
        forward(30)
        right(90)
    right(360 / 6)  # 绘制一个长方形后右转
done()  # 绘制结束
