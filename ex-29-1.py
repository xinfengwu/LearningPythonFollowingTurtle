#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n - 1) + n


print(sum(50))
print(sum(100))
