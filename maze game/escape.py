import turtle

class Escape:
    def __init__(self):
        self.block = turtle.Turtle()
        self.block.shape("square")
        self.block.color("green")
        self.block.penup()

        self.position = (200, 200)
        self.block.goto(self.position)