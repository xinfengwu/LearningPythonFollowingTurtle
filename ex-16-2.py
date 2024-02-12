#!/usr/bin/env python
# -*- coding: utf-8 -*-

h = float(input('请输入身高（米）： '))
w = float(input('请输入体重（千克）： '))
BMI = h / (w * w)
if BMI < 18.5:
    print('偏瘦')
elif BMI >= 18.5 and BMI < 24:
    print('正常')
elif BMI >= 24 and BMI < 30:
    print('超重')
else:
    print('肥胖')
