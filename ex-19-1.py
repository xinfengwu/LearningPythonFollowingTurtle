#!/usr/bin/env python
# -*- coding: utf-8 -*-

xlist = []
for i in range(1, 300):
    if i % 13 == 2 and i % 2 == 0:
        xlist.append(i)
print(xlist)
