#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fac(n):
    if n > 1:
        f = n * fac(n - 1)
    elif n == 1:
        f = 1
    return f


print(fac(4))
