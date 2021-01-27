# Lab 6

# Try to run this file. It should draw a scene. Your job is to make some
# corrections to the scene.  This turtle was called Speedy.

# 1. Speedy is really slow, make him go faster so it doesn't take so long.
# 2. There is a stray line from the corner of the house up to the roof,
#    make it go away.
# 3. Put a purple door on the house.
# 4. The grass is really long. Cut it by making it shorter.
# 5. Make it sunset -- the sun should be halfway below the horizon and
#    the sky should be darker. If you draw it first, then you can cover
#    it up with other stuff later.
# 6. Put your name in the picture after the name of the college.

# Feel free to make any other artistic changes if you wish.

# When you are done, take a screenshot of the result to turn in along
# with the updated code file.


import turtle



def drawScene():
    speedy = turtle.Turtle()  ## construct a turtle to use
    speedy.penup()  ## draw later
    speedy.speed(0) ## choose how fast to run speedy, 10 is fast, 0 is fastest


    ## upper portion of screen is sky -- 8 different colors to make sunset.
        
    # Color 1 (first 4 are yellowish tones)
    speedy.goto(-400, -100)     ##  go to lower left corner of sky.
    speedy.color('yellow')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(800)
        speedy.left(90)
        speedy.forward(50)
        speedy.left(90)
    speedy.end_fill()

    # Color 2
    speedy.goto(-400, -50)     ##  go to lower left corner of sky.
    speedy.color('gold')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(800)
        speedy.left(90)
        speedy.forward(50)
        speedy.left(90)
    speedy.end_fill()

    # Color 3
    speedy.goto(-400, 0)     ##  go to lower left corner of sky.
    speedy.color('khaki')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(800)
        speedy.left(90)
        speedy.forward(50)
        speedy.left(90)
    speedy.end_fill()

    # Color 4
    speedy.goto(-400, 50)     ##  go to lower left corner of sky.
    speedy.color('pale goldenrod')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(800)
        speedy.left(90)
        speedy.forward(50)
        speedy.left(90)
    speedy.end_fill()

    # Color 5 (Blue section)
    speedy.goto(-400, 100)     ##  go to lower left corner of sky.
    speedy.color('light cyan')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(800)
        speedy.left(90)
        speedy.forward(50)
        speedy.left(90)
    speedy.end_fill()

    # Color 6
    speedy.goto(-400, 150)     ##  go to lower left corner of sky.
    speedy.color('pale turquoise')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(800)
        speedy.left(90)
        speedy.forward(50)
        speedy.left(90)
    speedy.end_fill()

    # Color 7
    speedy.goto(-400, 200)     ##  go to lower left corner of sky.
    speedy.color('sky blue')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(800)
        speedy.left(90)
        speedy.forward(50)
        speedy.left(90)
    speedy.end_fill()

    # Color 8
    speedy.goto(-400, 250)     ##  go to lower left corner of sky.
    speedy.color('cornflower blue')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(800)
        speedy.left(90)
        speedy.forward(50)
        speedy.left(90)
    speedy.end_fill()

    
    ## lower part of house -- a salmon-colored rectangle
    speedy.goto(0, -100)     ##  go to lower left corner of window.
    speedy.color('salmon')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(300)
        speedy.left(90)
        speedy.forward(160)
        speedy.left(90)
    speedy.end_fill()

    ##  the roof
    speedy.penup()
    speedy.color('tan')
    for x in range(-30, 330, 4):    ##  draw a sequence of line segments
        speedy.goto(150, 150)       ##  peak of roof
        speedy.pendown()
        speedy.goto(x, 60)          ##  point along drip edge
    speedy.penup()

    ## purple door
    speedy.goto(175, -100)
    speedy.pendown()
    speedy.color('purple')
    speedy.begin_fill()
    speedy.left(90)
    for i in range (2):
        speedy.forward(100)
        speedy.left(90)
        speedy.forward(50)
        speedy.left(90)
    speedy.right(90)
    speedy.end_fill()
    speedy.penup()
    
    ##  sun in the sky

    speedy.goto(-200, -100)
    speedy.pendown()
    speedy.color('white', 'gold')
    speedy.begin_fill()
    for i in range(18):
        speedy.forward(90)      # We will make the sun bigger
        speedy.right(170)
    speedy.end_fill()
    speedy.penup()
    speedy.right(180)

    ## lower portion of screen is ground -- a brown rectangle
    speedy.goto(-400, -300)     ##  go to lower left corner of window.
    speedy.color('sienna')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle -- 
        speedy.forward(800)     ##  long side
        speedy.left(90)
        speedy.forward(200)     ##  short side
        speedy.left(90)
    speedy.end_fill()
    
    ##  grass
    speedy.goto(-400, -100)         ##  left end, where ground meets sky
    speedy.color('green')   
    for x in range(-400, 400, 6):   ##  iterate through blades
        speedy.left(85)             ##  leans slightly
        speedy.pendown()
        speedy.forward(15)          ##  draw blade, how large the grass is. 
        speedy.penup()
        speedy.right(180)           ##  turn around
        speedy.forward(15)          ##  traced over it again
        speedy.left(95)
        speedy.forward(6)
    speedy.penup()

    ##  add a greeting
    speedy.color('white')
    speedy.goto(-300, -200)
    speedy.pendown()
    speedy.write("Bethany Lutheran College     ", align='center', font=('Arial', 12, 'normal'))
    speedy.penup()
    
    ## My name
    speedy.goto(-300, -240)
    speedy.pendown()
    speedy.write("Nuria Perez Casas", align='center', font=('Arial', 20, 'bold'))

    speedy.penup()
    speedy.goto(-500,-500)
if __name__ == "__main__":
    drawScene()

