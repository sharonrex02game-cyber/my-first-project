import turtle
import time

class Player:
    def __init__(self, walls, escape, start_time):
        self.player = turtle.Turtle()
        self.player.shape("square")
        self.player.color("blue")
        self.player.penup()
        self.start_time = start_time


        self.speed = 20
        self.walls = walls.wall_positions
        self.escape = escape

    def check_escape(self):
        pos = (self.player.xcor(), self.player.ycor())

        if pos == self.escape.position:
            end_time = time.time()
            total = round(end_time - self.start_time, 2)

            message = turtle.Turtle()
            message.hideturtle()
            message.color("white")
            message.penup()

            message.write(
                f"you escaped!\nTime: {total}s",
                align="center",
                font=("Arial", 16, "normal")
            )


    def up(self):
        x = self.player.xcor()
        y = self.player.ycor() + self.speed

        if (x, y) not in self.walls:
            self.player.sety(y)
        self.check_escape()

    def down(self):
        x = self.player.xcor()
        y = self.player.ycor() - self.speed

        if (x, y) not in self.walls:
            self.player.sety(y) 

        self.check_escape()

    def left(self):
        x = self.player.xcor() - self.speed
        y = self.player.ycor()

        if (x, y) not in self.walls:
            self.player.setx(x)
        self.check_escape()

    def right(self):
        x = self.player.xcor() + self.speed
        y = self.player.ycor()

        if (x, y) not in self.walls:
            self.player.setx(x)

        self.check_escape()


    def controles(self, screen):
        screen.listen()
        screen.onkeypress(self.up, "w")
        screen.onkeypress(self.down, "s")
        screen.onkeypress(self.left, "a")
        screen.onkeypress(self.right, "d")