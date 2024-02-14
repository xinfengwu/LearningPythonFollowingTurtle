#!/usr/bin/env python
# -*- coding: utf-8 -*-


def Sum(a, b):
    return a + b


x = int(input('请输入整数1： '))
y = int(input('请输入整数2： '))
z = int(input('请输入整数3： '))
print(Sum(Sum(x, y), z))
