from turtle import Turtle

class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score=0
        self.penup()
        self.color('white')
        self.ht()
        self.goto(position)
        self.write(self.score,align='center',font=('Courier',18,'bold'))

    def in_line(self):
        # for _ in range(400):
        turtle=Turtle()
        turtle.ht()
        turtle.color('white')
        turtle.shapesize(2)
        turtle.goto(0,300)
        turtle.goto(0,-300)

    def edit_score(self):
        self.score+=1
        self.clear()
        self.write(self.score, align='center', font=('alex brush', 18, 'bold'))


