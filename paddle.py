from turtle import Turtle
# POSITIONS_1=(-270,0)
# POSITIONS_2=[(270,0),(270,20),(270,40)]

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        # self = Turtle()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(5, 1)
        self.goto(position)
        # self.padds.append(self)
        # self.create_paddle(POSITIONS_1)
        # self.create_paddle(POSITIONS_2)
        # self.padds=[]


    # def create_paddle(self,position):
        # for position in positions:
      

    def up(self):
        new_y_cor= self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)

    # def fast(self):
    #     self.fast(0)


