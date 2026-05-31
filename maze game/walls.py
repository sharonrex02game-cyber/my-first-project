import turtle

class Walls:
    def __init__(self):
        self.wall_positions = [
            (-100, 100),
            (-80, 100),
            (-60, 100),
            (0, 0),
            (20, 0)

        ]


        self.walls = []

        for position in self.wall_positions:
            wall = turtle.Turtle()
            wall.shape("square")
            wall.color("brown")
            wall.penup()
            wall.goto(position)


            self.walls.append(wall)