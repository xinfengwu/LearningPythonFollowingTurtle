#!/usr/bin/env python
# -*- coding: utf-8 -*-

score = int(input('请输入得分： '))
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('中等')
elif score >= 60:
    print('及格')
else:
    print('不及格')
