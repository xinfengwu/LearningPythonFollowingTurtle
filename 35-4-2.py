#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle

h = 600
w = 800
turtle.setup(width=w, height=h)
turtle.bgpic('background.gif')
birdImage = 'bird.gif'
turtle.addshape(birdImage)
turtle.shape(birdImage)
turtle.showturtle()
turtle.done()
