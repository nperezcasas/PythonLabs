# Nuria Perez Casas
# COMS 103
# Lab 2

import turtle
nu = turtle.Turtle()
nu.shape("turtle")
nu.speed(10)
nu.penup()
nu.goto(-300,300)
nu.pendown()
nu.color("black","red")
nu.width(40)

#We just made all the setup we need to start with our first letter. Letter B.
#We could probably have done it a little bit easier but I like the aesthetics this way.
nu.right(90)
nu.forward(200)
nu.begin_fill()
nu.left(90)
nu.forward(100)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(75)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(100)
nu.right(180)
nu.forward(100)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(75)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(100)

#Now we'll proceed with the L, much less complicated than letter B. 
nu.penup()
nu.goto(-50,300)
nu.pendown()
nu.left(90)
nu.forward(200)
nu.left(90)
nu.forward(100)

#Now we'll draw the C
nu.penup()
nu.goto(275,300)
nu.pendown()
nu.left(180)
nu.forward(30)
nu.circle(100,180)
nu.forward(30)

#Now we will write"introduction to programming# in the center of the image
#I changed the font and made it bold to look more alike to the BLC letters. 
nu.penup()
nu.goto(-250,0)
nu.write("Introduction to Programming", font=("Cooper", 36, "bold"))


#Now to make it a little bit more fancy and more alike the BLC logo letters
#We will repeat the process of the letters but this time it is going to be
#with color red and with the width smaller so that it looks like the actual logo.
#New setup 
nu.penup()
nu.goto(-300,300)
nu.pendown()
nu.color("red","black")
nu.width(25)

#B in red
nu.right(90)
nu.forward(200)
nu.left(90)
nu.forward(100)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(75)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(100)
nu.right(180)
nu.forward(100)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(75)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(100)

#L in red
nu.penup()
nu.goto(-50,300)
nu.pendown()
nu.left(90)
nu.forward(200)
nu.left(90)
nu.forward(100)

#C in red
nu.penup()
nu.goto(275,300)
nu.pendown()
nu.left(180)
nu.forward(30)
nu.circle(100,180)
nu.forward(30)


#To do it still more alike we will now do the last layer of it, in white.
#And this time we will go from C to B to change things up a little bit. 
#C in white
nu.color("white","red")
nu.width(18)
nu.penup()
nu.goto(275,300)
nu.pendown()
nu.left(180)
nu.forward(30)
nu.circle(100,180)
nu.forward(30)

#L in white
nu.penup()
nu.goto(-50,300)
nu.pendown()
nu.right(90)
nu.forward(200)
nu.left(90)
nu.forward(100)

#B in red
nu.penup()
nu.goto(-300,300)
nu.pendown()
nu.right(90)
nu.forward(200)
nu.left(90)
nu.forward(100)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(75)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(100)
nu.right(180)
nu.forward(100)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(75)
nu.left(45)
nu.forward(20)
nu.left(45)
nu.forward(100)

#Now we will finish up with a cute little star in our bottom right corner. 
nu.speed(1000)
nu.penup()
nu.goto(200,-175)
nu.pendown()
nu.color("red")
nu.width(30)
for i in range(100):
    nu.forward(150)
    nu.right(144)

#Hope you liked it! :)

