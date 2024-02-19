#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


# 自定义函数，接收参数为鼠标位置处x，y坐标
def draw(x, y):
    goto(x, y)


# 当鼠标点击时，调用fun函数
onscreenclick(draw)
done()
