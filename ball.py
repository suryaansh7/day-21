from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10


    def move(self,):
        xcord=self.xcor()+self.x_move
        ycord=self.ycor()+self.y_move
        self.penup()
        self.goto(xcord,ycord)
        self.pendown()


    def collide(self):
        self.y_move*=-1
    def bounce1(self):
        self.x_move*=-1
    def reset(self):
        self.penup()
        self.goto(0,0)
        self.pendown()






