import time
import turtle
import random

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.starting_position=(0,-280)
        self.step_size=10
        self.finish_line_Y=280
        self.color_list=['#8B0000','#006400','#4B0082','#D2691E','#191970']
        self.shape('turtle')
        self.penup()
        self.color(random.choice(self.color_list))
        self.new_start()
        self.left(90)
    def go_up(self):
        self.forward(self.step_size)
    def go_left(self):
        self.goto(self.xcor() - self.step_size, self.ycor())
    def go_right(self):
        self.goto(self.xcor() + self.step_size, self.ycor())
    def go_down(self):
        self.goto(self.xcor(), self.ycor() - self.step_size)
    def is_finished(self):
        if self.ycor() > self.finish_line_Y:
            return True
        else:
            return False
    def new_start(self):
        self.goto(self.starting_position)

class Car:
    def __init__(self):
        self.all_cars = []
        self.step_size = 4
        self.color_list = ['#FF0000', '#9400D3', '#FFD700', 'red','yellow','#ADFF2F', '#00BFFF', '#6495ED', '#FF6347','#BA55D3','#32CD32']
    def make_car(self):
        new_car = turtle.Turtle("square")
        new_car.shapesize(stretch_wid=1 ,stretch_len=2)
        new_car.color(random.choice(self.color_list))
        new_car.penup()
        random_y = random.randint(-240,240)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)
    def move(self):
        for car in self.all_cars:
            if car.xcor() < -300:
                car.hideturtle()
            else:
                car.backward(self.step_size)
    def level_up(self):
        self.step_size += 1

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,265)
        self.declare()
    def level_up(self):
        self.clear()
        self.level += 1
        self.declare()
    def declare(self):
        self.write(f"Level:{self.level}",align="left",font=('Courier',18,'normal'))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align="center",font=('Courier',18,'normal'))
    def winner(self):
        self.goto(0,0)
        self.write("🎉 CONGRATULATIONS 🎉\nYou Are The Winner",align="center",font=('Courier',18,'normal'))

def make_border(width, height, color):
    border_maker = turtle.Turtle()
    border_maker.penup()
    border_maker.goto((-width-8)/2,(height+8)/2)
    border_maker.color(color)
    border_maker.pensize(8)
    border_maker.pendown()
    border_maker.hideturtle()
    for j in range(2):
        border_maker.forward(width+8)
        border_maker.right(90)
        border_maker.forward(height+8)
        border_maker.right(90)

screen=turtle.Screen()
w = 600
h = 600
screen.setup(width = w,height = h)
screen.tracer(0)
make_border(w,h,'black')

player=Player()
car_generator = Car()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(player.go_up,"Up")
screen.onkeypress(player.go_left,"Left")
screen.onkeypress(player.go_right,"Right")
screen.onkeypress(player.go_down,"Down")

game_on=True
count = 0
car_spawn_speed = 6

while game_on:
    if car_spawn_speed <= 1:
        scoreboard.winner()
        for cars in car_generator.all_cars:
            time.sleep(0.01)
            cars.hideturtle()
        game_on=False
    time.sleep(0.1)
    screen.update()
    if random.randint(1,car_spawn_speed) == 1:
        car_generator.make_car()
    car_generator.move()

    for car in car_generator.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    if player.is_finished():
        player.new_start()
        car_spawn_speed -= 1
        car_generator.level_up()
        scoreboard.level_up()


screen.exitonclick()
