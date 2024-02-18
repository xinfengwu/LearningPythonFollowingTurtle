#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
import random


# 定义函数绘制树干（树干长度）
def drawBranch(branchLength):
    color('saddle brown')
    if branchLength > 2:  # 如果树干长度大于5
        pensize(branchLength / 20)  # 树干越短，越细
        # 绘制当前branchLength长度的树干
        forward(branchLength)
        # 绘制右边的子树干，要短15
        angleRight = random.randint(10, 30)  # 右边随机角度
        right(angleRight)
        drawBranch(branchLength - random.randint(10, 20))
        # 绘制左边的子树干，要短15
        angleLeft = random.randint(10, 30)  # 左边随机角度
        left(angleRight + angleLeft)
        drawBranch(branchLength - random.randint(10, 20))
        # 回到当前树干的起点
        right(angleLeft)
        backward(branchLength)
    else:  # 绘制末端的叶子
        colors = ['pink', 'red']
        color(colors[random.randint(0, 1)])
        dot(5)
        color('saddle brown')


speed(8)
penup()
goto(0, -200)
setheading(90)
pendown()
drawBranch(100)
done()
