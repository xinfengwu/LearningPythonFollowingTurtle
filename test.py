import turtle

# 创建画布
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("red")

# 创建海龟对象
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# 绘制五星红旗
def draw_china_flag():
    # 绘制大五角星
    t.penup()
    t.goto(-100, 50)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(200)
        t.right(144)
    t.end_fill()
    
    # 绘制四个小五角星
    t.penup()
    t.goto(-60, 110)
    t.pendown()
    for _ in range(4):
        t.begin_fill()
        for _ in range(5):
            t.forward(25)
            t.right(144)
        t.end_fill()
        t.penup()
        t.forward(50)
        
    # 绘制横幅
    t.penup()
    t.goto(-100, 30)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    for _ in range(2):
        t.forward(200)
        t.right(90)
        t.forward(40)
        t.right(90)
    t.end_fill()

# 绘制中国国旗
draw_china_flag()

# 保持窗口打开
turtle.done()

