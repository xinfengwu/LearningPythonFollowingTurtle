#!/usr/bin/env python
# -*- coding: utf-8 -*-

psd = ''
while psd != '1234':
    psd = input("请输入密码： ")
    print(psd)
    print('密码错误！')
print(psd)
print('密码正确！')
