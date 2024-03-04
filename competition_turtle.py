from turtle import Turtle,Screen,TK
import random
screen=Screen()
is_race_on = False
screen.setup(500,400)
user_bet = screen.textinput(title="what your bet?" , prompt="Which turtle win the competition?(green,purple,red,blue,yellow,black)")
y = -125
ind = 0
turtle_color_list = ["green","purple","red","blue","yellow","black"]
turtle_list =[]
for turtlee in turtle_color_list:
    turtlee = Turtle(shape="turtle")
    turtlee.penup()
    turtlee.shape("turtle")
    turtlee.color(turtle_color_list[ind])
    turtle_list.append(turtlee)
    turtlee.goto(-230,y)
    ind +=1
    y += 50
if user_bet in turtle_color_list:
    is_race_on = True
    
while is_race_on:
    for check in turtle_list:
        if check.xcor() >= 250.0:
            is_race_on = False
            if check.color()[0] == user_bet:
                TK.messagebox.showinfo(title="The Turtle says:", message="congrulations, winner is you")
            else:
                TK.messagebox.showinfo(title="The Turtle says:", message=f"You are loser.Winner is {check.color()[0]}")
                
    turt = random.choice(turtle_list)
    distance = random.randint(1,10)
    turt.forward(distance)
    
screen.exitonclick()

