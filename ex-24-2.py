#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fun(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


print(fun(50))
print(fun(100))
