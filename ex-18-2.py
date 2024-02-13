#!/usr/bin/env python
# -*- coding: utf-8 -*-

nums = [23, 57, 39, 88, 75, 63, 26]
sum = 0
for i in range(7):
    if i % 2 == 0:
        sum += nums[i]
print(sum)
