#!/usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(1, 3000):
    if i % 5 == 1 and i % 6 == 5 and i % 7 == 4 and i % 11 == 10:
        print(i)
