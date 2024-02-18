#!/usr/bin/env python
# -*- coding: utf-8 -*-


def funA():
    print("A")


def funB():
    funA()
    print('B')


funB()
