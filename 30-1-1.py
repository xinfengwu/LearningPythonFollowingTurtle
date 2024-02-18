#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 定义函数绘制树干（树干长度）
def drawBranch(branchLength):
    if branchLength > 5:  # 如果树干长度大于5
        # 绘制当前branchLength长度的树干
        forward(branchLength)
        # 绘制右边的子树干，要短15
        right(20)
        drawBranch(branchLength - 15)
        # 绘制左边的子树干，要短15
        left(40)
        drawBranch(branchLength - 15)
        # 回到当前树干的起点
        right(20)
        backward(branchLength)


speed(0)
penup()
goto(0, -200)
setheading(90)
pendown()
drawBranch(100)
done()
