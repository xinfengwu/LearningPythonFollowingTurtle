#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *


def fun(x, y):
    print('鼠标左键点加位置：', x, ' ', y)


# 当鼠标点击时，调用fun函数
onscreenclick(fun)
done()
