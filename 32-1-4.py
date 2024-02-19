#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fun():
    global x
    x = 5
    print('函数内： ', x)


x = 10
fun()
print('函数外： ', x)
