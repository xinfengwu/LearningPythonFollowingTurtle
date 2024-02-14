import turtle

# 创建画布
screen = turtle.Screen()
screen.setup(width=600, height=600)

# 创建画笔
pen = turtle.Turtle()
pen.speed(2)  # 设置速度

# 设置线条颜色为黄色
pen.color("yellow")

# 画五角星
for _ in range(5):
    pen.forward(100)
    pen.right(144)

# 创建填充画笔
fill_pen = turtle.Turtle()
fill_pen.speed(0)  # 设置填充画笔速度为最快

# 移动到五角星中心并开始填充
fill_pen.penup()
fill_pen.goto(pen.pos())
fill_pen.pendown()

# 设置填充颜色为紫色
fill_pen.fillcolor("purple")

# 开始填充
fill_pen.begin_fill()

# 画五角星
for _ in range(5):
    fill_pen.forward(100)
    fill_pen.right(144)

# 结束填充
fill_pen.end_fill()

# 隐藏填充画笔
fill_pen.hideturtle()

# 关闭画布时继续显示
screen.mainloop()

