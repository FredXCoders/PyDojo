'''
  python tutorial module for the FredX CodeDojo.

  This module handles the setup process of the turtle module to minimize typing for beginners.
  Letter functions have been defined to print "HELLO WORLD" graphically on the screen.  Additional fun
  shapes and designs have been added to allow the kids to create some cool effects by stringing them together.

  if module is run it will print Hello World message in colors and arrow keys will move the turtle around once
  the window is active (by clicking it).  Clicking in the window will stamp a turtle in that spot. The q key
  will quit the program.

  to use this module for coding use the "from fredx import *" to import the module contents into the namespace.
  Importing this way allows functions to be used without pre-pending the "fredx." module name.

  author: sabadam32
'''
import turtle

# Re-assign movement functions for less typing
lt = turtle.lt
rt = turtle.rt
fd = turtle.fd
back = turtle.back

# Re-assign drawing functions for less typing
pu = turtle.pu
pd = turtle.pd
bf = turtle.begin_fill
ef = turtle.end_fill
fc = turtle.fillcolor
cl = turtle.clear
circle = turtle.circle

# Letters are all designed to fit 40 W x 110 H with a 10 W space after the letter making the total width 50
# Letters should also advance the turtle to the bottom right of the letter space in prep for the next letter.
def h(fill=False):
    '''draws a capital H.
     This is a DOCstring, which is a special comment that DOCuments our code.  When you type help() in python it
     displays these strings.  Don't take my word for it... try it yourself!'''
    turtle.setheading(0)
    if fill: bf()
    fd(10)
    lt(90)
    fd(50)
    rt(90)
    fd(20)
    rt(90)  # These things after the .'s are functions we can use, just like this h function!
    fd(50)
    lt(90)
    fd(10)
    lt(90)
    fd(110)
    lt(90)
    fd(10)
    lt(90)
    fd(50)
    rt(90)
    fd(20)
    rt(90)
    fd(50)
    lt(90)
    fd(10)
    lt(90)
    fd(110)
    lt(90)
    if fill: ef()  # single statement 'if' can be put on the same line
    pu()
    fd(50)
    pd()

def e(fill=False):
    '''draws a capital E.  Docstrings need to be the first line in a function definition'''
    turtle.setheading(0)
    if fill: bf()
    fd(40)
    lt(90)
    fd(10)
    lt(90)
    fd(30)
    rt(90)
    fd(40)
    rt(90)
    fd(30)
    lt(90)
    fd(10)
    lt(90)
    fd(30)
    rt(90)
    fd(40)
    rt(90)
    fd(30)
    lt(90)
    fd(10)
    lt(90)
    fd(40)
    lt(90)
    fd(110)
    lt(90)
    if fill: ef()
    pu()
    fd(50)
    pd()

def l(fill=False):
    '''draws a capital L.  Doctrings must use the multi-line comment format.'''
    turtle.setheading(0)
    if fill: bf()
    fd(40)
    lt(90)
    fd(10)
    lt(90)
    fd(30)
    rt(90)
    fd(100)
    lt(90)
    fd(10)
    lt(90)
    fd(110)
    lt(90)
    if fill: ef()
    pu()
    fd(50)
    pd()

def o(fill=False):
    '''draws a capital O'''
    turtle.setheading(0)
    pu()
    fd(20)
    pd()
    if fill: bf()
    circle(20, 90)
    fd(70)
    circle(20, 180)
    fd(70)
    circle(20, 90)
    if fill: ef()
    pu()
    turtle.sety(turtle.ycor() + 10)
    pd()
    cfc = fc()
    fc(turtle.getscreen().bgcolor())
    bf()
    circle(10, 90)
    fd(70)
    circle(10, 180)
    fd(70)
    circle(10, 90)
    ef()
    pu()
    turtle.goto(turtle.xcor() + 30, turtle.ycor() - 10)
    pd()
    fc(cfc)

def w(fill=False):
    '''draws a capital W.'''
    turtle.setheading(0)
    pu()
    turtle.sety(turtle.ycor() + 110)
    pd()
    if fill: bf()
    turtle.goto(turtle.xcor() + 10, turtle.ycor() - 110)
    turtle.goto(turtle.xcor() + 5, turtle.ycor())
    turtle.goto(turtle.xcor() + 5, turtle.ycor() + 50)
    turtle.goto(turtle.xcor() + 5, turtle.ycor() - 50)
    turtle.goto(turtle.xcor() + 5, turtle.ycor())
    turtle.goto(turtle.xcor() + 10, turtle.ycor() + 110)
    turtle.goto(turtle.xcor() - 10, turtle.ycor())
    turtle.goto(turtle.xcor() - 5, turtle.ycor() - 55)
    turtle.goto(turtle.xcor() - 2, turtle.ycor() + 20)
    turtle.goto(turtle.xcor() - 6, turtle.ycor())
    turtle.goto(turtle.xcor() - 2, turtle.ycor() - 20)
    turtle.goto(turtle.xcor() - 5, turtle.ycor() + 55)
    turtle.goto(turtle.xcor() - 10, turtle.ycor())
    if fill: ef()
    pu()
    turtle.goto(turtle.xcor() + 50, turtle.ycor() - 110)
    pd()

def r(fill=False):
    '''draws a capital R.'''
    turtle.setheading(0)
    if fill: bf()
    fd(10)
    lt(90)
    fd(50)
    rt(90)
    turtle.goto(turtle.xcor() + 20, turtle.ycor() - 50)
    fd(10)
    turtle.goto(turtle.xcor() - 20, turtle.ycor() + 50)
    circle(20, 90)
    fd(20)
    circle(20, 90)
    fd(20)
    lt(90)
    fd(110)
    if fill: ef()
    pu()
    turtle.goto(turtle.xcor() + 10, turtle.ycor() + 60)
    pd()
    lt(90)
    cfc = fc()
    fc(turtle.getscreen().bgcolor())
    bf()
    fd(10)
    circle(10, 90)
    fd(20)
    circle(10, 90)
    fd(10)
    lt(90)
    fd(40)
    ef()
    fc(cfc)
    lt(90)
    pu()
    turtle.goto(turtle.xcor() + 40, turtle.ycor() - 60)
    pd()

def d(fill=False):
    '''draws a capital D'''
    turtle.setheading(0)
    if fill: bf()
    fd(20)
    circle(20, 90)
    fd(70)
    circle(20, 90)
    fd(20)
    lt(90)
    fd(110)
    lt(90)
    if fill: ef()
    pu()
    turtle.goto(turtle.xcor() + 10, turtle.ycor() + 10)
    pd()
    cfc = fc()
    fc(turtle.getscreen().bgcolor())
    bf()
    fd(10)
    circle(10, 90)
    fd(70)
    circle(10, 90)
    fd(10)
    lt(90)
    fd(90)
    ef()
    lt(90)
    pu()
    turtle.goto(turtle.xcor() + 40, turtle.ycor() - 10)
    pd()
    fc(cfc)

def a(fill=False):
    '''draws a capital A.'''
    turtle.setheading(0)
    if fill: bf()
    fd(10)
    turtle.goto(turtle.xcor() + 5, turtle.ycor() + 40)
    fd(10)
    turtle.goto(turtle.xcor() + 5, turtle.ycor() - 40)
    fd(10)
    turtle.goto(turtle.xcor() - 15, turtle.ycor() + 110)
    turtle.setx(turtle.xcor() - 10)
    turtle.goto(turtle.xcor() - 15, turtle.ycor() - 110)
    if fill: ef()
    pu()
    turtle.goto(turtle.xcor() + 17, turtle.ycor() + 50)
    pd()
    if fill:
        cfc = fc()
        fc(turtle.getscreen().bgcolor())
        bf()
    fd(6)
    turtle.goto(turtle.xcor() - 3, turtle.ycor() + 40)
    turtle.goto(turtle.xcor() - 3, turtle.ycor() - 40)
    if fill:
        ef()
        fc(cfc)
    pu()
    turtle.goto(turtle.xcor() + 33, turtle.ycor() - 50)
    pd()


def draw_letters(fill=False, color=None, *letters):
    '''Draws a series of letters'''
    if fill and color:fc(color)
    for letter in letters:
        letter(fill)

def hello():
    '''draws hello world message in rainbow colors'''
    turtle.setheading(0)
    pu()
    turtle.setx(-265)
    pd()
    draw_letters(True, "red", h)
    draw_letters(True, "dark orange", e)
    draw_letters(True, "yellow", l)
    draw_letters(True, "green", l)
    draw_letters(True, "blue", o)
    pu()
    turtle.setx(turtle.xcor() + 30)
    draw_letters(True, "blue", w)
    draw_letters(True, "blue violet", o)
    draw_letters(True, "violet", r)
    draw_letters(True, "pink", l)
    draw_letters(True, "red", d)

def hola():
    '''draws hola world message in cool green color'''
    turtle.setheading(0)
    pu()
    turtle.setx(-215)
    pd()
    draw_letters(True, "green", h, o, l, a)
    pu()
    turtle.setx(turtle.xcor() + 30)
    draw_letters(True, "green", w, o, r, l, d)

# Shapes
def square(size=100):
    '''draws a square'''
    for i in range(4):
        fd(size)
        lt(90)

def rectangle(size=100):
    '''draws a rectangle'''
    for i in range(2):
        fd(size)
        lt(90)
        fd(size/2)
        lt(90)

def hexagon(size=100):
    '''draws a hexagon'''
    for i in range(6):
        fd(size)
        lt(60)

def octagon(size=100):
    '''draws an octagon'''
    for i in range(8):
        fd(size)
        lt(45)

def triangle(size=100):
    '''draws a triangle'''
    for i in range(3):
        fd(size)
        lt(120)

def flower():
    '''Draws a flower like thing on the screen'''
    for i in range(8):
        rt(45)
        for j in range(6):
            turtle.tracer(False)
            for k in range(90):
                fd(1)
                rt(2)
            rt(90)
            turtle.tracer(True,10)

def star(size=100):
    '''Draws a star'''
    for i in range(12):
        fd(size)
        lt(150)

def loops(size=100,func=circle):
    '''Draws loops using the shape function'''
    for i in range(45):
        func(size)
        lt(8)

def house(size=100,dcolor='dark red',hcolor='tan'):
    '''draws a house'''
    half = size*.5
    door = size*.6
    oc = color()
    fc(hcolor)
    bf()
    square(size)
    ef()
    fd(half + (door*.25))
    lt(90)
    fc(dcolor)
    bf()
    rectangle(door)
    ef()
    pu()
    rt(90)
    back(half + (door*.25))
    lt(90)
    fd(size)
    rt(90)
    pd()
    fc(hcolor)
    bf()
    triangle(size)
    ef()
    pu()
    rt(90)
    fd(size)
    lt(90)
    color(oc[0])
    fc(oc[1])
    pd()

def tree():
    '''draw a tree'''
    oc = color()
    fc('saddle brown')
    bf()
    turtle.goto(turtle.xcor()+20,turtle.ycor())
    turtle.goto(turtle.xcor(),turtle.ycor()+80)
    turtle.goto(turtle.xcor()-20,turtle.ycor())
    turtle.goto(turtle.xcor(),turtle.ycor()-80)
    ef()
    fc('dark green')
    color('dark green')
    pu()
    turtle.goto(turtle.xcor()+10,turtle.ycor()+80)
    pd()
    bf()
    circle(20)
    ef()
    turtle.goto(turtle.xcor()-20,turtle.ycor()-20)
    bf()
    circle(20)
    ef()
    pu()
    turtle.goto(turtle.xcor()+40,turtle.ycor())
    pd()
    bf()
    circle(20)
    ef()
    pu()
    turtle.goto(turtle.xcor()-30,turtle.ycor()-60)
    pd()
    color(oc[0])
    fc(oc[1])

#Setup stuff
def begin():
    '''Starts up the turtle screen and sets up the turtle object'''
    sc = turtle.Screen()
    sc.title("Am I not turtley enough for you.  Turtle, turtle, turtle.")
    sc._root.attributes("-topmost", 1)  # hack to get the window to show in front of the terminal
    #sc._root.attributes("-topmost", 0)

    if __name__ == "__main__":
        sc.setup(1.0, 1.0)  # make screen full window
        sc.onkey(go_up, "Up")
        sc.onkey(go_down, "Down")
        sc.onkey(go_left, "Left")
        sc.onkey(go_right, "Right")
        sc.onkey(quit, "q")

    turtle.speed(0)
    turtle.shape("turtle")
    fc("light blue")

def rs():
    '''moves turtle back to center clears screen and resets the turtle object'''
    turtle.reset()
    begin()

# Movement Functions

#movement based on turtles heading (Direction)
def mvf(step=10):
    '''moves the turtle forward along heading without drawing'''
    pu()
    fd(step)
    pd()

def mvb(step=10):
    '''moves the turtle back along heading without drawing'''
    pu()
    bk(step)
    pd()

def mvl(step=10):
    '''moves the turtle to the left (up perpendicular from heading on screen) without drawing'''
    pu()
    lt(90)
    fd(step)
    rt(90)
    pd()

def mvr(step=10):
    '''moves the turtle to the right (down perpendicular from heading on screen) without drawing'''
    pu()
    rt(90)
    fd(step)
    lt(90)
    pd()

def mvlf(step=10):
    '''moves the turtle diagonally left(up) and forward from heading without drawing'''
    pu()
    lt(45)
    fd(step)
    rt(45)
    pd()

def mvlb(step=10):
    '''moves the turtle diagonally left(up) and back from heading without drawing'''
    pu()
    lt(135)
    fd(step)
    rt(135)
    pd()

def mvrf(step=10):
    '''moves the turtle diagonally right(down) and forward without drawing'''
    pu()
    rt(45)
    fd(step)
    lt(45)
    pd()

def mvrb(step=10):
    '''moves the turtle diagonally right(down) and back from heading without drawing'''
    pu()
    rt(135)
    fd(step)
    lt(135)
    pd()

#movement based on screen coordinates
def mve(step=10):
    '''moves the turtle east(right) without drawing'''
    pu()
    turtle.setx(turtle.xcor()+step)
    pd()

def mvw(step=10):
    '''moves the turtle west(left) without drawing'''
    pu()
    turtle.setx(turtle.xcor()-step)
    pd()

def mvn(step=10):
    '''moves the turtle north(up) without drawing'''
    pu()
    turtle.sety(turtle.ycor()+step)
    pd()

def mvs(step=10):
    '''moves the turtle south(down) without drawing'''
    pu()
    turtle.sety(turtle.ycor()-step)
    pd()

def mvne(step=10):
    '''moves the turtle northeast without drawing'''
    pu()
    turtle.goto(turtle.xcor()+step,turtle.ycor()+step)
    pd()

def mvnw(step=10):
    '''moves the turtle northwest without drawing'''
    pu()
    turtle.goto(turtle.xcor()-step,turtle.ycor()+step)
    pd()

def mvsw(step=10):
    '''moves the turtle southwest without drawing'''
    pu()
    turtle.goto(turtle.xcor()-step,turtle.ycor()-step)
    pd()

def mvse(step=10):
    '''moves the turtle southeast without drawing'''
    pu()
    turtle.goto(turtle.xcor()+step,turtle.ycor()-step)
    pd()


if __name__ == "__main__":
    def go_up():
        '''Moves turtle up on the screen when up arrow is pressed'''
        turtle.setheading(90)
        fd(10)

    def go_right():
        '''Moves turtle right on screen when right arrow is pressed'''
        turtle.setheading(0)
        fd(10)

    def go_left():
        '''Moves turtle left on screen when left arrow is pressed'''
        turtle.setheading(180)
        fd(10)

    def go_down():
        '''Moves turtle down on screen when down arrow is pressed'''
        turtle.setheading(270)
        fd(10)

    def stampit(eks,why):
        '''moved the turtle to the position on the screen that was clicked and stamps itself'''
        pu()
        turtle.goto(eks,why)
        turtle.stamp()
        pd()

    #Global Turtle ready to... run
    begin()

    turtle.bgcolor('black')
    hello()
    turtle.getscreen().listen() #allows us to collect key events to move turtle, but window must be active window.
    turtle.onscreenclick(stampit)
    turtle.mainloop()
