import turtle
import time
import random

# Variables
delay = 0.1
score = 0
high_score = 0
game_started = False

# Set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)


# snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"
head.hideturtle() # Hide until game starts

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
food.hideturtle() # Hide until game starts

segments = []

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

def start_game():
    global game_started
    if not game_started:
        game_started = True
        pen.clear()
        head.showturtle()
        food.showturtle()

def go_up():
    if head.direction != "down": head.direction = "up"

def go_down():
    if head.direction != "up": head.direction = "down"

def go_left():
    if head.direction != "right": head.direction = "left"

def go_right():
    if head.direction != "left": head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

def reset_game():
    global score, delay
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    delay = 0.1
    update_score()

def update_score():
    pen.clear()
    pen.goto(0, 260)
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

def show_menu():
    pen.clear()
    pen.goto(0, 50)
    pen.write("SNAKE GAME", align="center", font=("Courier", 40, "bold"))
    pen.goto(0, -20)
    pen.write("Press 'Space' to Play", align="center", font=("Courier", 20, "normal"))
    pen.goto(0, -60)
    pen.write("W/A/S/D to Move", align="center", font=("Courier", 15, "italic"))

# Keyboard
window.listen()
window.onkeypress(start_game, "space")
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# menu
show_menu()


while True:
    window.update()

    if game_started:
        # Check for border collision
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            reset_game()

        # Check for food collision
        if head.distance(food) < 20:
            food.goto(random.randint(-280, 280), random.randint(-280, 280))
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("lightgreen")
            new_segment.penup()
            segments.append(new_segment)
            score += 10
            if score > high_score: high_score = score
            update_score()

        for index in range(len(segments)-1, 0, -1):
            segments[index].goto(segments[index-1].xcor(), segments[index-1].ycor())
        if len(segments) > 0:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        for segment in segments:
            if segment.distance(head) < 20:
                reset_game()

        time.sleep(delay)
