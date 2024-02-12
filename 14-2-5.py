#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = int(input('请输入整数1： '))
y = int(input('请输入整数2： '))
z = int(input('请输入整数3： '))
if x >= y and x >= z:
    print('三个数的最大值是： ', x)
if y >= x and y >= x:
    print('三个数的最大值是： ', y)
if z >= x and z >= y:
    print('三个数的最大值是： ', z)
