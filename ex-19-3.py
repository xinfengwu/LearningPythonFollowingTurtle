#!/usr/bin/env python
# -*- coding: utf-8 -*-

oddlist = []
evenlist = []
for i in range(10):
    x = int(input('请输入整数：'))
    if x % 2 == 0:
        evenlist.append(x)
    else:
        oddlist.append(x)
print(oddlist)
print(evenlist)
