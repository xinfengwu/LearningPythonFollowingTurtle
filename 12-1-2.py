#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle库

shape('turtle')
c = input('请输入颜色字符串： ')  # 输入设定颜色
color(c)  #设置绘制颜色
# 以下循环绘制正方形
for i in range(4):
    forward(150)  # 前进
    right(90)  # 右转
done()
