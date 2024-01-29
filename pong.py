from turtle import Turtle
class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        # self.shapesize(.5,.5)
        self.color('white')
        self.xco=10
        self.yco=20
        self.move_speed=0.1
        # self.seth(30)

    def move(self):
        X_cor=self.xcor()+self.xco
        Y_cor=self.ycor()+self.yco
        self.goto(X_cor,Y_cor)

    def bounce_y(self):
     self.yco*=-1

    def bounce_x(self):
        self.xco*=-1
        self.move_speed*=0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()

    # def bounce_off_left_paddle(self):
    #     self.yco *= -1
    #     self.xco *= -1

    # def bounce_up(self):
    #     self.yco *= -1
    #
    # def bounce_up(self):
    #     X_cor = self.xcor() - 10
    #     Y_cor = self.ycor() + 10
    #     self.goto(X_cor, Y_cor)