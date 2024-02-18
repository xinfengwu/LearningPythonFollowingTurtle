#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

a = 0
b = 0
for i in range(1000):
    n = random.randint(1, 2)
    if n == 1:
        a += 1
    else:
        b += 1
print('硬币正面朝上次数： ', a, '反面朝上次数： ', b)
