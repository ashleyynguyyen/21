import turtle
import random
#set up turtles
person = turtle.Turtle()
person.penup()
person.goto(0, -300)
wn = turtle.Screen()
wn.title("Cross the Road")
goal=turtle.Turtle()
goal.color('lime')
goal.fillcolor('lime')
goal.pu()
goal.hideturtle()
score_writer = turtle.Turtle()
score_writer.penup()
score_writer.hideturtle()
score=0
score_writer.goto(-190,240)
score_writer.pendown()
font_setup=("Arial", 20, "normal")
#background and score position
turtle.Screen().bgcolor("#808080")
road_width = 50
road_lines = turtle.Turtle()
road_lines.penup()
road_lines.color("yellow")
road_lines.speed('fastest')
road_lines.pendown()
number_of_lines = 40
road_lines.width(5)
x=0
wn.tracer(False)
def draw_lane():
    global x
    x=0
    while x < number_of_lines:
        road_lines.pendown()
        road_lines.forward(800/(2*number_of_lines))
        road_lines.penup()
        road_lines.forward(800/(2*number_of_lines))
        road_lines.pendown()
        x=x+1
y=2
number_of_lanes = 6
while y<number_of_lanes:
    road_lines.setheading(0)
    road_lines.penup()
    road_lines.goto(-400,300-y*80)
    draw_lane()
    y=y+1
road_lines.penup()
road_lines.goto(-400,220)
road_lines.pendown()
road_lines.forward(800)
road_lines.penup()
road_lines.goto(-400,-180)
road_lines.pendown()
road_lines.forward(800)
goal.goto(-100,300)
goal.pd()
goal.begin_fill()
goal.forward(200)
goal.right(90)
goal.forward(50)
goal.right(90)
goal.forward(200)
goal.right(90)
goal.forward(50)
goal.end_fill()
wn.tracer(True)
#timer
timer = 40
counter_interval =1000  
timer_up = False
counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(180,240)
counter.pendown()
 
#functions for collision and person movement
def forward():
    person.setheading(90)
    person.forward(20)
def right():
    person.setheading(0)
    person.forward(20)
def left():
    person.setheading(180)
    person.forward(20)
def backward():
    person.setheading(270)
    person.forward(20)
def collision():
    person.hideturtle()
    person.goto(0, -200)
    person.showturtle()
def update_score():
    global score
    score +=1
    score_writer.clear()
    score_writer.write(score, font= font_setup)
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
      counter.write("Time's Up", font=font_setup)
      timer_up = True
      person.hideturtle()
    else:
     counter.write("Timer: " + str(timer), font=font_setup)
     timer -= 1
     counter.getscreen().ontimer(countdown, counter_interval) 
def run_game():
    global timer, timer_up
    countdown()
    if timer_up != True:
        wn.onkeypress(forward, 'Up')
        wn.onkeypress(right, 'Right')
        wn.onkeypress(left, 'Left')
        wn.onkeypress(backward, 'Down')
 
#person movement
person.penup()
person.speed("fastest")
 
run_game()
wn.listen()
 
#list of cars
a_cars = []
b_cars = []
c_cars = []
d_cars = []
e_cars = []
 
#add a_cars
for _ in range(4):
    a_car = turtle.Turtle()
    a_car.speed(0)
    a_car.shape("square")
    a_car.color("blue")
    a_car.penup()
    a_car.goto(0, 20)
    a_car.speed = random.randint(10, 20)
    a_cars.append(a_car)
 
#add b_cars
for _ in range(4):
    b_car = turtle.Turtle()
    b_car.speed(0)
    b_car.shape("square")
    b_car.color("pink")
    b_car.penup()
    b_car.goto(0, 40)
    b_car.speed = random.randint(10, 20)*-1
    b_cars.append(b_car)
 
    #add c_cars
for _ in range(4):
    c_car = turtle.Turtle()
    c_car.speed(0)
    c_car.shape("square")
    c_car.color("purple")
    c_car.penup()
    c_car.goto(0, 40)
    c_car.speed = random.randint(10, 20)
    c_cars.append(c_car)
 
    #add d_cars
for _ in range(4):
    d_car = turtle.Turtle()
    d_car.speed(0)
    d_car.shape("square")
    d_car.color("green")
    d_car.penup()
    d_car.goto(0, 40)
    d_car.speed = random.randint(10, 20)*-1 
    d_cars.append(d_car)
 
    #add e_cars
for _ in range(4):
    e_car = turtle.Turtle()
    e_car.speed(0)
    e_car.shape("square")
    e_car.color("orange")
    e_car.penup()
    e_car.goto(0, 40)
    e_car.speed = random.randint(10, 20)
    e_cars.append(e_car)
 
#main game loop 
while True:
    #update screen
    wn.update()
    #move the a_cars
    for a_car in a_cars:
        if (abs(person.xcor()-a_car.xcor())<20) and abs(person.ycor()-a_car.ycor())<20:
            collision()     
        x = a_car.xcor()
        x-= a_car.speed
        a_car.setx(x)
 
        #off screen respawn
        if x < -300:
            y = random.randint(90, 120)
            x = random.randint (480, 480)
            a_car.goto(x, y)
 
    #move the b_cars
    for b_car in b_cars: 
        if (abs(person.xcor()-b_car.xcor())<20) and abs(person.ycor()-b_car.ycor())<20:
            collision()          
        x = b_car.xcor()
        x-= b_car.speed
        b_car.setx(x)
 
        #off screen respawn
        if x > 300:
            y = random.randint(160, 200)
            x = random.randint (480, 480)
            b_car.goto(-x, y)
            
    #move the c_cars
    for c_car in c_cars:
        if (abs(person.xcor()-c_car.xcor())<20) and abs(person.ycor()-c_car.ycor())<20:
            collision()       
        x = c_car.xcor()
        x-= c_car.speed
        c_car.setx(x)
 
        #off screen respawn
        if x < -300:
            y = random.randint(10, 40)
            x = random.randint (480, 480)
            c_car.goto(x, y)
 
    #move the d_cars
    for d_car in d_cars:
        if (abs(person.xcor()-d_car.xcor())<20) and abs(person.ycor()-d_car.ycor())<20:
            collision()           
        x = d_car.xcor()
        x-= d_car.speed
        d_car.setx(x)
 
        #off screen respawn
        if x > 300:
            y = random.randint(-80, -40)
            x = random.randint (480, 480)
            d_car.goto(-x, y)
 
    #move the e_cars
    for e_car in e_cars:
        if (abs(person.xcor()-e_car.xcor())<20) and abs(person.ycor()-e_car.ycor())<20:
            collision()          
        x = e_car.xcor()
        x-= e_car.speed
        e_car.setx(x)
 
        #off screen respawn
        if x < -300:
            y = random.randint(-170, -110)
            x = random.randint (480, 480)
            e_car.goto(x, y)
    
    #update score when reaching the goal
    if (abs(person.xcor()-goal.xcor())<215) and abs(person.ycor()-goal.ycor())<50:
            update_score()
            collision()
 
wn.mainloop()
