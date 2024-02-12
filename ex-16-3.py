#!/usr/bin/env python
# -*- coding: utf-8 -*-

year = int(input('出生年份： '))
if year % 4 == 0 and year % 100 != 0:
    print('是闰年')
elif year % 100 == 0 and year % 400 == 0:
    print('是闰年')
else:
    print('不是闰年')
