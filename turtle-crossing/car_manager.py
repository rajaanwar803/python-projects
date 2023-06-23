from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        y_position = random.randrange(-240, 240, 80)
        self.goto(300, y_position)
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE)

    def increase_distance(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())
