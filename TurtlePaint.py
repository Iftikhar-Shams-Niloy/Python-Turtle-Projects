import turtle
player = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('#DCDCDC')

#Writing Instructions#
instruction = turtle.Turtle()
instruction.penup()
instruction.goto(-800,300)
instruction.pendown()
instruction.color("black")
font_style = ("Times new roman",12,"bold")
instruction.write("""
Use 'W','A','S','D' for moving
Use 1,2,3,4,5,6 for changin color
Use ',' for pen-up and '.' for pen-down
Use '=' for clearing the screen 
""", font=font_style, align='left')

def make_box():
    instruction.pensize(2.5)
    instruction.backward(20)
    f1 = 260
    f2 = 90
    for i in range(2):
        f1 += 20
        f2 += 20
        for j in range(2):
            instruction.forward(f1)
            instruction.left(90)
            instruction.forward(f2)
            instruction.left(90)
        instruction.color('#FFD700')
        instruction.penup()
        instruction.backward(10)
        instruction.right(90)
        instruction.forward(10)
        instruction.left(90)
        instruction.pendown()
    instruction.hideturtle()

make_box()

player.pensize(5)
player.shape('turtle')

def black():
    player.color('black')
def red():
    player.color('red')
def blue():
    player.color('blue')
def green():
    player.color('green')
def yellow():
    player.color('yellow')
def orange():
    player.color('orange')

def move_forwards():
    player.forward(10)
def move_left():
    player.left(3)
def move_right():
    player.right(3)
def move_back():
    player.backward(10)
def clear():
    player.home()
    player.clear()
def pen_up():
    player.penup()
def pen_down():
    player.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="s", fun=move_back)
screen.onkey(key="1", fun=black)
screen.onkey(key="2", fun=red)
screen.onkey(key="3", fun=blue)
screen.onkey(key="4", fun=green)
screen.onkey(key="5", fun=yellow)
screen.onkey(key="6", fun=orange)
screen.onkey(key="=", fun=clear)
screen.onkey(key=",", fun=pen_up)
screen.onkey(key=".", fun=pen_down)

screen.exitonclick()
