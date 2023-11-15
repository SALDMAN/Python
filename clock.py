import turtle
import time

# Set up the turtle screen and the turtle object
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Analog Clock")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# Draw the clock face
def draw_clock_face(radius):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.goto(0, 0)
    t.pendown()

    for i in range(12):
        t.penup()
        t.goto(0, 0)
        t.right(i * 30)
        t.forward(radius - 20)
        t.pendown()
        t.write(i or 12, align="center", font=("Arial", 16, "normal"))

# Draw the clock hands
def draw_clock_hands(hour, minute, second, radius):
    # Hour hand
    t.penup()
    t.goto(0, 0)
    t.color("white")
    t.setheading(90)
    t.right(hour * 30 + minute * 0.5)
    t.pendown()
    t.forward(radius * 0.5)

    # Minute hand
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.right(minute * 6)
    t.pendown()
    t.forward(radius * 0.7)

    # Second hand
    t.penup()
    t.goto(0, 0)
    t.color("red")
    t.setheading(90)
    t.right(second * 6)
    t.pendown()
    t.forward(radius * 0.9)

# Continuously update the clock hands
while True:
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    draw_clock_face(250)
    draw_clock_hands(hour, minute, second, 250)

    wn.update()
    t.clear()

wn.mainloop()