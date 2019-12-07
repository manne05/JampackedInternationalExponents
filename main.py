import turtle, random

#Defining the turtles for all of the boxes
box1 = turtle.Turtle()
box1.ht()
box1.speed("fastest")

box2 = turtle.Turtle()
box2.ht()
box2.speed('fastest')

box3 = turtle.Turtle()
box3.ht()
box3.speed('fastest')

box4 = turtle.Turtle()
box4.ht()
box4.speed('fastest')

box5 = turtle.Turtle()
box5.ht()
box5.speed('fastest')

#Defining everything for the player turtle
player=turtle.Turtle()
player.speed('fastest')
player.shape('turtle')
player.color('white')
player.fillcolor('black')
player.pu()

#Global variable defining
box1x = 1
box1y = 1
box2x = 1
box2y = 1
box3x = 1
box3y = 1
box4x = 1
box4y = 1
box5x = 1
box5y = 1
redboxx = 1
redboxy = 1
score = 0


#Defines everything for the red boxes
redx = []
redy = []
redbox = turtle.Turtle()
redbox.ht()
redbox.speed(0)

#Sets the background color to purple
window=turtle.Screen()
window.bgcolor("dark slate blue")

#Sets the border color and white square on the inside
border = turtle.Turtle()
border.speed(0)
border.penup()
border.goto(-250,-250)
border.pendown()
border.color('black')
border.begin_fill()
border.pensize(3)
for i in range(4):
  border.forward(500)
  border.left(90)
border.color('honeydew')
border.end_fill()
border.ht()

#Creates the score box at the top of the screen and starts score off with 000
scorebox = turtle.Turtle()
scorenum = turtle.Turtle()
scorenum.ht()
scorebox.ht()
scorebox.pu()
scorebox.speed(0)
scorebox.goto(-50,265)
scorebox.pensize(3)
scorebox.pd()
scorebox.begin_fill()
for i in range(2):
  scorebox.forward(100)
  scorebox.left(90)
  scorebox.forward(50)
  scorebox.left(90)
scorebox.color('honeydew')
scorebox.end_fill()
scorenum.pu()
scorenum.goto(scorebox.xcor(),scorebox.ycor())
scorenum.forward(15)
scorenum.left(90)
scorenum.forward(10)
scorenum.pd()
scorenum.color('black')
scorenum.write("000" , move=False, font=("Arial", 30, "normal"))

#Moves player left when left arrow hit
def left(): 
  for i in range(0,3):
    if player.xcor() <= -230:
      player.setheading(180)
    else:
      player.setheading(180)
      player.forward(3)
  check()

#Moves player right when right arrow hit
def right():
  for i in range(0,3):
    if player.xcor() >= 230:
      player.setheading(0)
    else:
      player.setheading(0)
      player.forward(3)
  check()

#Moves player up when up arrow hit
def up(): 
  for i in range(0,3):
    if player.ycor() >= 230:
      player.setheading(90)
    else:
      player.setheading(90)
      player.forward(3)
  check()

#Moves player down when down arrow hit
def down():
  for i in range(0,3):
    if player.ycor() <=-230:
      player.setheading(270)
    else:
      player.setheading(270)
      player.forward(3)
  check()

#Just for testing to get coords
def c():
  print(player.xcor(),player.ycor())

#Functions that check if the box is making contact with the player
def check1():
  if player.xcor() < box1x +24 and player.xcor() > box1x -24 and player.ycor() < box1y +24 and player.ycor() > box1y -24:
    return("contact")
  else:
    return("nocontact")
def check2():
  if player.xcor() < box2x +24 and player.xcor() > box2x -24 and player.ycor() < box2y +24 and player.ycor() > box2y -24:
    return("contact")
  else:
    return("nocontact")
def check3():
  if player.xcor() < box3x +24 and player.xcor() > box3x -24 and player.ycor() < box3y +24 and player.ycor() > box3y -24:
    return("contact")
  else:
    return("nocontact")
def check4():
  if player.xcor() < box4x +24 and player.xcor() > box4x -24 and player.ycor() < box4y +24 and player.ycor() > box4y -24:
    return("contact")
  else:
    return("nocontact")
def check5():
  if player.xcor() < box5x +24 and player.xcor() > box5x -24 and player.ycor() < box5y +24 and player.ycor() > box5y -24:
    return("contact")
  else:
    return("nocontact")

def checkred():
  global redx
  global redy
  for i in range(len(redx)):
    if player.xcor() < redx[i] + 30 and player.xcor() > redx[i] - 30 and player.ycor() < redy[i] + 30 and player.ycor() > redy[i] - 30:
      return("contact")
  return("nocontact")

#Checks which of the boxes were hit by running the functions above and looking at return values
def check():
  if check1() == 'contact':
    box1.clear()
    box1draw()
    scoreadd()
    redboxdraw()
  if check2() == 'contact':
    box2.clear()
    box2draw()
    scoreadd()
    redboxdraw()
  if check3() == 'contact':
    box3.clear()
    box3draw()
    scoreadd()
    redboxdraw()
  if check4() == 'contact':
    box4.clear()
    box4draw()
    scoreadd()
    redboxdraw()
  if check5() == 'contact':
    box5.clear()
    box5draw()
    scoreadd()
    redboxdraw()
  if checkred() == 'contact':
    endgame()

#Rewrites the score in the score box 
def scoreadd():
  global score
  print("Box collected!")
  scorenum.clear()
  score += 1
  scorenum.pd()
  if score <= 9:
    scorenum.write("00" + str(score) , move=False, font=("Arial", 30, "normal"))
  elif score <= 99:
    scorenum.write("0" + str(score) , move=False, font=("Arial", 30, "normal"))
  else:
    scorenum.write(str(score) , move=False, font=("Arial", 30, "normal"))

#Getting coords for first box
def box1co():
  global box1x
  global box1y
  while True:
    box1x = random.randint(-200,200)
    box1y = random.randint(-200,200)
    if box1x < 50 and box1x > -50 and box1y > -50 and box1y < 50 or box1x < player.xcor() + 25 and box1x > player.xcor() - 25 and box1y < player.ycor() + 25 and box1y > player.ycor - 25:
      box1x = random.randint(-200,200)
      box1y = random.randint(-200,200)
    else: 
      break


#Getting coords for second box
def box2co():
  global box2x
  global box2y
  while True:
    box2x = random.randint(-200,200)
    box2y = random.randint(-200,200)
    if box2x < box1x +100 and box2x > box1x -100 and box2y < box1y +100 and box2y > box1y -100 or box2x < player.xcor() + 25 and box2x > player.xcor() - 25 and box2y < player.ycor() + 25 and box2y > player.ycor() - 25:
      box2x = random.randint(-200,200)
      box2y = random.randint(-200,200)
    else:
      break

#Getting coords for third box
def box3co():
  global box3x
  global box3y
  while True:
    box3x = random.randint(-200,200)
    box3y = random.randint(-200,200)
    if box3x < box1x +100 and box3x > box1x -100 and box3y < box1y +100 and box3y > box1y -100 or box3x < box2x +100 and box3x > box2x -100 and box3y < box2y +100 and box3y > box2y -100 or box3x < player.xcor() + 25 and box3x > player.xcor() - 25 and box3y < player.ycor() + 25 and box3y > player.ycor() - 25:
      box3x = random.randint(-200,200)
      box3y = random.randint(-200,200)
    else:
      break

#Getting coords for fourth box
def box4co():
  global box4x
  global box4y
  while True:
    box4x = random.randint(-200,200)
    box4y = random.randint(-200,200)
    if box4x < box1x +100 and box4x > box1x -100 and box4y < box1y +100 and box4y > box1y -100 or box4x < box2x +100 and box4x > box2x -100 and box4y < box2y +100 and box4y > box2y -100 or box4x < box3x +100 and box4x > box3x -100 and box4y < box3y +100 and box4y > box3y -100 or box4x < player.xcor() + 25 and box4x > player.xcor() - 25 and box4y < player.ycor() + 25 and box4y > player.ycor() - 25:
      box4x = random.randint(-200,200)
      box4y = random.randint(-200,200)
    else:
      break

#Getting coords for fifth box
def box5co():
  global box5x
  global box5y
  while True:
    box5x = random.randint(-200,200)
    box5y = random.randint(-200,200)
    if box5x < box1x +100 and box5x > box1x -100 and box5y < box1y +100 and box5y > box1y -100 or box5x < box2x +100 and box5x > box2x -100 and box5y < box2y +100 and box5y > box2y -100 or box5x < box3x +100 and box5x > box3x -100 and box5y < box3y +100 and box5y > box3y -100 or box5x < box4x +100 and box5x > box4x -100 and box5y < box4y +100 and box5y > box4y -100 or box5x < player.xcor() + 25 and box5x > player.xcor() - 25 and box5y < player.ycor() + 25 and box5y > player.ycor() - 25:
      box5x = random.randint(-200,200)
      box5y = random.randint(-200,200)
    else:
      break

#Getting coords for red box
def redboxco():
  global redboxx
  global redboxy
  while True:
    redboxx = random.randint(-225,225)
    redboxy = random.randint(-225,225)
    if redboxx < box1x +50 and redboxx > box1x -50 and redboxy < box1y +50 and redboxy > box1y -50 or redboxx < box2x +50 and redboxx > box2x -50 and redboxy < box2y +50 and redboxy > box2y -50 or redboxx < box3x +50 and redboxx > box3x -50 and redboxy < box3y +50 and redboxy > box3y -50 or redboxx < box4x +50 and redboxx > box4x -50 and redboxy < box4y +50 and redboxy > box4y -50 or redboxx < box5x +50 and redboxx > box5x -50 and redboxy < box5y +50 and redboxy > box5y -50 or redboxx < player.xcor() + 25 and redboxx > player.xcor() - 25 and redboxy < player.ycor() + 25 and redboxy > player.ycor() - 25:
      for i in range(len(redx)):
        if redboxx < redx[i] + 100 and redboxx > redx[i] - 100 and redboxy < redy[i] + 100 and redboxy > redy[i] - 100:
          redboxx = random.randint(-225,225)
          redboxy = random.randint(-225,225)
    else:
      break

#Draws the first box
def box1draw(): 
  box1co()
  box1.penup()
  box1.goto(box1x,box1y)
  box1.pendown()
  box1.left(90)
  box1.penup()
  box1.forward(10)
  box1.pendown()
  box1.right(90)
  box1.begin_fill()
  box1.forward(10)
  for i in range(3):
    box1.right(90)
    box1.forward(20)
  box1.right(90)
  box1.forward(10)
  box1.color('yellow green')
  box1.end_fill()
  box1.color('black')

#Draws the second box
def box2draw():
  box2co()
  box2.penup()
  box2.goto(box2x,box2y)
  box2.pendown()
  box2.left(90)
  box2.penup()
  box2.forward(10)
  box2.pendown()
  box2.right(90)
  box2.begin_fill()
  box2.forward(10)
  for i in range(3):
    box2.right(90)
    box2.forward(20)
  box2.right(90)
  box2.forward(10)
  box2.color('yellow green')
  box2.end_fill()
  box2.color('black')

#Draws the third box
def box3draw():
  box3co()
  box3.penup()
  box3.goto(box3x,box3y)
  box3.pendown()
  box3.left(90)
  box3.penup()
  box3.forward(10)
  box3.pendown()
  box3.right(90)
  box3.begin_fill()
  box3.forward(10)
  for i in range(3):
    box3.right(90)
    box3.forward(20)
  box3.right(90)
  box3.forward(10)
  box3.color('yellow green')
  box3.end_fill()
  box3.color('black')

#Draws the fourth box
def box4draw():
  box4co()
  box4.penup()
  box4.goto(box4x,box4y)
  box4.pendown()
  box4.left(90)
  box4.penup()
  box4.forward(10)
  box4.pendown()
  box4.right(90)
  box4.begin_fill()
  box4.forward(10)
  for i in range(3):
    box4.right(90)
    box4.forward(20)
  box4.right(90)
  box4.forward(10)
  box4.color('yellow green')
  box4.end_fill()
  box4.color('black')

#Draws the fifth box
def box5draw():
  box5co()
  box5.penup()
  box5.goto(box5x,box5y)
  box5.pendown()
  box5.left(90)
  box5.penup()
  box5.forward(10)
  box5.pendown()
  box5.right(90)
  box5.begin_fill()
  box5.forward(10)
  for i in range(3):
    box5.right(90)
    box5.forward(20)
  box5.right(90)
  box5.forward(10)
  box5.color('yellow green')
  box5.end_fill()
  box5.color('black')

#Draws the red box
def redboxdraw():
  global redx
  global redy
  global redboxx
  global redboxy
  redboxco()
  print(redboxx, redboxy)
  redx.append(redboxx)
  redy.append(redboxy)
  redbox.penup()
  redbox.goto(redboxx,redboxy)
  redbox.pendown()
  redbox.left(90)
  redbox.penup()
  redbox.forward(20)
  redbox.pendown()
  redbox.right(90)
  redbox.begin_fill()
  redbox.forward(20)
  for i in range(3):
    redbox.right(90)
    redbox.forward(40)
  redbox.right(90)
  redbox.forward(20)
  redbox.color('fire brick')
  redbox.end_fill()
  redbox.color('black')

#Endgame functions that stops player from moving, sets screen to white, and tells you your score.
def endgame():
  global end
  global redx
  global redy
  print("Endgame")
  keys_deactivate()
  border = turtle.Turtle()
  border.speed(0)
  border.penup()
  border.goto(-250,-250)
  border.pendown()
  border.color('black')
  border.begin_fill()
  border.pensize(3)
  for i in range(4):
    border.forward(500)
    border.left(90)
  border.color('honeydew')
  player.ht()
  redx = []
  redy = []
  border.end_fill()
  border.ht()
  box1.clear()
  box2.clear()
  box3.clear()
  box4.clear()
  box5.clear()
  scorenum.left(90)
  scorenum.forward(4)
  scorenum.pd()
  scorenum.clear()
  scorenum.write('END' , move=False, font=("Arial", 30, "normal"))
  final_score = turtle.Turtle()
  final_score.ht()
  final_score.pu()
  final_score.speed(0)
  final_score.goto(-120,20)
  final_score.write("Deine Punkte:" , move=False, font=("Arial", 40, "normal"))
  final_score.goto(-40,-50)
  final_score.pd()
  if score <= 9:
    final_score.write("00" + str(score) , move=False, font=("Arial", 40, "normal"))
  elif score <= 99:
    final_score.write("0" + str(score) , move=False, font=("Arial", 40, "normal"))
  else:
    final_score.write(str(score) , move=False, font=("Arial", 40, "normal"))

#Calls all functions to draw original boxes
box1draw()
box2draw()
box3draw()
box4draw()
box5draw()
redboxdraw()

#Linking the keys pressed to the function, and starts watching to see if any keys are pressed
def keys_activate():
  window.onkey(left, "Left")
  window.onkey(right, "Right")
  window.onkey(up, "Up")
  window.onkey(down, "Down")
  window.onkey(c, "C")

#I put them in functions so that I could deactivate the use of keys once you die.
def keys_deactivate():
  window.onkey(None, "Left")
  window.onkey(None, "Right")
  window.onkey(None, "Up")
  window.onkey(None, "Down")
  window.onkey(None, "C")

#Calls the keys to activate and starts listening
keys_activate()
window.listen()
window.mainloop()
