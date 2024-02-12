#!/usr/bin/env python
# -*- coding: utf-8 -*-

month = int(input('请输入一个月份： '))

if month == 3 or month == 4 or month == 5:
    print('是春季')
elif month == 6 or month == 7 or month == 8:
    print('是夏季')
elif month == 9 or month == 10 or month == 11:
    print('是秋季')
else:
    print('是冬季')
