#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *  # 导入turtle库

c = input('请输入颜色字符串首字母： ')
if c == 'r':  # 如果输入'r'，就设置为红色
    color('red')  # 设置绘制颜色
if c == 'R':  # 如果输入'R'，就设置为红色
    color('red')  # 设置绘制颜色
# 以下循环绘制正方形
for i in range(4):
    forward(150)  # 前进
    right(90)  # 右转
done()  # 绘制结束
