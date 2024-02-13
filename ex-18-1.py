#!/usr/bin/env python
# -*- coding: utf-8 -*-

nums = [23, 57, 39, 88, 75, 63]
odd = 0
even = 0
for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print('奇数个数： ' + str(odd) + '个', '偶数个数： ' + str(even) + '个。')
