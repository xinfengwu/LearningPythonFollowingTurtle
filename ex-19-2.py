#!/usr/bin/env python
# -*- coding: utf-8 -*-

fib = [1, 1]
for i in range(13):
    fib.append(fib[i] + fib[i + 1])
print(fib)
