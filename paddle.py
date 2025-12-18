from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,xcord,ycord):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(10, 2)


        self.goto(xcord, ycord)
        self.pendown()


    def up(self):
        xcord1 = self.xcor()
        ycord1 = self.ycor()
        self.penup()
        self.goto(xcord1, ycord1 + 20)

    def down(self):
        xcord2 = self.xcor()
        ycord2 = self.ycor()
        self.penup()
        self.goto(xcord2, ycord2 - 20)



