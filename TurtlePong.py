import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG!')

class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        custom_shape= ((-12, 0), (-10, 10), (10, 10), (12, 0), (10, -10), (-10, -10))
        turtle.register_shape('diamond',custom_shape)
        self.shape('diamond')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    def go_up(self):
        self.goto(self.xcor(), self.ycor()+20)
    def go_down(self):
        self.goto(self.xcor(),self.ycor()-20)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.shape('circle')
        self.penup()
        self.x_step= 2
        self.y_step= 5
    def move(self):
        new_x = self.xcor()+ self.x_step
        new_y = self.ycor()+ self.y_step
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_step = -self.y_step
    def bounce_x(self):
        self.x_step = -(self.x_step + self.x_step*0.1)
    def reset_position(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.bounce_x()
        if self.x_step <0:
            self.x_step = -2
        else:
            self.x_step = 2
        self.y_step= random.choice([-3,-2,-1,1,2,3])

class ScoreBoard(turtle.Turtle):
    def __init__(self, p1, p2):
        super().__init__()
        self.color('red')
        self.penup()
        self.hideturtle()
        self.p1 = p1
        self.p2 = p2
        self.player1_score = 0
        self.player2_score = 0
        self.update()
        self.winner = None
    def update(self):
        text1 = "|"+ self.p1 +" : "+ str(self.player1_score)+"|"
        text2 = "|"+ self.p2 +" : "+ str(self.player2_score)+"|"
        self.goto(-120,240)
        self.write( text1, align='center', font=('Comic Sans MS',20,'normal'))
        self.goto(120,240)
        self.write( text2,align='center',font=('Comic Sans MS',20,'normal'))
    def player1_point(self):
        self.player1_score += 1
        self.clear()
        self.update()
    def player2_point(self):
        self.player2_score += 1
        self.clear()
        self.update()
    def check_winner(self):
        if self.player1_score >= 5:
            self.winner = self.p1
            return True
        elif self.player2_score >= 5:
            self.winner = self.p2
            return True
        else:
            return False

border_maker = turtle.Turtle()
border_maker.penup()
border_maker.goto(-400,300)
border_maker.color('white')
border_maker.pensize(8)
border_maker.pendown()
border_maker.hideturtle()

for j in range(2):
    border_maker.forward(800)
    border_maker.right(90)
    border_maker.forward(600)
    border_maker.right(90)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
p1 = turtle.textinput("Enter Your NAME","Player1 Name")
p2 = turtle.textinput("Enter Your NAME","Player2 Name")
scoreboard= ScoreBoard(p1,p2)

screen.listen()
screen.onkey(key='Up', fun=right_paddle.go_up)
screen.onkey(key='Down', fun=right_paddle.go_down)
screen.onkey(key='w', fun=left_paddle.go_up)
screen.onkey(key='s', fun=left_paddle.go_down)



game_on = True
winner_found = False

while game_on:
    check = scoreboard.check_winner()
    if check == True:
        winner_found = True
        game_on = False
        break
    else:
        screen.update()
        ball.move()
        #Check if winner found
        #Detecting Collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if ball.distance(right_paddle)<50 and ball.xcor()>330 or ball.distance(left_paddle)<50 and ball.xcor()<-330:
            ball.bounce_x()
        if ball.xcor()>380:
            ball.reset_position()
            scoreboard.player1_point()
        if ball.xcor()<-380:
            ball.reset_position()
            scoreboard.player2_point()

if winner_found:
    screen.clear()
    screen.bgcolor('black')
    win_declare = turtle.Turtle()
    win_declare.color('white')
    win_declare.write(("Congratulations "+ scoreboard.winner + "!\nYou are the winner!!!"), align='center', font=('Comic Sans MS',40,'normal'))
    win_declare.penup()
    win_declare.hideturtle()

screen.exitonclick()