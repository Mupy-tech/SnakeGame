import turtle
import time
import random

#creating the screen
screen = turtle.Screen()
screen.title("Mupy's hungry snake")
screen.setup(width=1000, height=1000)
screen.bgcolor("cyan")
screen.tracer(0)

#creating the snake head
head = turtle.Turtle()
head.penup()
head.shape("circle")
head.color("green")
head.goto(0,0)
head.direction = "stop"
head.speed(0)

#food
food = turtle.Turtle()
food.penup()
food.shape("circle")
food.color("red")
x = random.randint(-400, 400)
y = random.randint(-400, 400)
food.goto(x,y)

#creating the body
snake = []



#moving function
def ka_den():
    head.direction = "den"
def sham_der():
    head.direction = "der"
def sar_kul():
    head.direction = "sar_kul"
def sar_se():
    head.direction = "sar_se"
#comand for movement
def so():
    if head.direction == "den":
        y = head.ycor()
        head.sety(y + 10)
    elif head.direction == "der":
        y = head.ycor()
        head.sety(y - 10)
    elif head.direction == "sar_kul":
        x = head.xcor()
        head.setx(x + 10)
    elif head.direction == "sar_se":
        x = head.xcor()
        head.setx(x - 10)


#programing the keys to move (key binding)
screen.listen()
screen.onkey(ka_den, "Up")
screen.onkey(sham_der, "Down")
screen.onkey(sar_kul, "Right")
screen.onkey(sar_se, "Left")


#main game loop
while True:
    screen.update()
    if head.distance(food) < 20:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.speed(0.1)
        
        snake.append(new_segment)
        #moving the end segments first in reverse order
    for index in range(len(snake)-1, 0, -1):
        x = snake[index-1].xcor()
        y = snake[index-1].ycor()
        snake[index].goto(x,y)
        #moving segment 0 to where head is
    if len(snake)>0:
        x = head.xcor()
        y = head.ycor()
        snake[0].goto(x,y)

    so()
    time.sleep(0.1)

screen.mainloop()