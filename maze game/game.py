import turtle
from player import Player
from walls import Walls
from escape import Escape
import time


start_time = time.time()

screen = turtle.Screen()
screen.title("Maze Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)                                         


walls = Walls()
escape = Escape()
player = Player(walls, escape, start_time)
player.controles(screen)

screen.mainloop()