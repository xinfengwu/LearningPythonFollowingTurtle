#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle库

shape('turtle')  # 显示海龟图标
# 外层循环，绘制6个旋转正方形
for i in range(6):
    # 内层循环，绘制一个正方形
    for j in range(4):
        forward(100)
        right(90)
    right(60)  # 右转60度
done()  # 绘制结束
