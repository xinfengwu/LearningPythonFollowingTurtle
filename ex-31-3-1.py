#!/usr/bin/env python
# -*- coding: utf-8 -*-

psd = '1234'
times = 0
while True:
    if psd != input('请输入密码： '):
        print(psd)
        print('密码错误！')
    else:
        print(psd)
        print('密码正确！')
        break
    times += 1
    print(times)
    if times >= 3:
        print('输错三次密码，已锁定！')
