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
'''
from turtle import *

__author__ = "sabadam32"

# Letters are all designed to fit 40 W x 110 H with a 10 W space after the letter making the total width 50
# Letters should also advance the turtle to the bottom right of the letter space in prep for the next letter.
def h(fill=False):
    '''draws a capital H.
     This is a DOCstring, which is a special comment that DOCuments our code.  When you type help() in python it
     displays these strings.  Don't take my word for it... try it yourself!'''
    setheading(0)
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
    setheading(0)
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
    setheading(0)
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
    setheading(0)
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
    sety(ycor() + 10)
    pd()
    cfc = fc()
    fc(getscreen().bgcolor())
    bf()
    circle(10, 90)
    fd(70)
    circle(10, 180)
    fd(70)
    circle(10, 90)
    ef()
    pu()
    goto(xcor() + 30, ycor() - 10)
    pd()
    fc(cfc)

def w(fill=False):
    '''draws a capital W.'''
    setheading(0)
    pu()
    sety(ycor() + 110)
    pd()
    if fill: bf()
    goto(xcor() + 10, ycor() - 110)
    goto(xcor() + 5, ycor())
    goto(xcor() + 5, ycor() + 50)
    goto(xcor() + 5, ycor() - 50)
    goto(xcor() + 5, ycor())
    goto(xcor() + 10, ycor() + 110)
    goto(xcor() - 10, ycor())
    goto(xcor() - 5, ycor() - 55)
    goto(xcor() - 2, ycor() + 20)
    goto(xcor() - 6, ycor())
    goto(xcor() - 2, ycor() - 20)
    goto(xcor() - 5, ycor() + 55)
    goto(xcor() - 10, ycor())
    if fill: ef()
    pu()
    goto(xcor() + 50, ycor() - 110)
    pd()

def r(fill=False):
    '''draws a capital R.'''
    setheading(0)
    if fill: bf()
    fd(10)
    lt(90)
    fd(50)
    rt(90)
    goto(xcor() + 20, ycor() - 50)
    fd(10)
    goto(xcor() - 20, ycor() + 50)
    circle(20, 90)
    fd(20)
    circle(20, 90)
    fd(20)
    lt(90)
    fd(110)
    if fill: ef()
    pu()
    goto(xcor() + 10, ycor() + 60)
    pd()
    lt(90)
    cfc = fc()
    fc(getscreen().bgcolor())
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
    goto(xcor() + 40, ycor() - 60)
    pd()

def d(fill=False):
    '''draws a capital D'''
    setheading(0)
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
    goto(xcor() + 10, ycor() + 10)
    pd()
    cfc = fc()
    fc(getscreen().bgcolor())
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
    goto(xcor() + 40, ycor() - 10)
    pd()
    fc(cfc)

def a(fill=False):
    '''draws a capital A.'''
    setheading(0)
    if fill: bf()
    fd(10)
    goto(xcor() + 5, ycor() + 40)
    fd(10)
    goto(xcor() + 5, ycor() - 40)
    fd(10)
    goto(xcor() - 15, ycor() + 110)
    setx(xcor() - 10)
    goto(xcor() - 15, ycor() - 110)
    if fill: ef()
    pu()
    goto(xcor() + 17, ycor() + 50)
    pd()
    if fill:
        cfc = fc()
        fc(getscreen().bgcolor())
        bf()
    fd(6)
    goto(xcor() - 3, ycor() + 40)
    goto(xcor() - 3, ycor() - 40)
    if fill:
        ef()
        fc(cfc)
    pu()
    goto(xcor() + 33, ycor() - 50)
    pd()


def draw_letters(fill=False, color=None, *letters):
    '''Draws a series of letters'''
    if fill and color:fc(color)
    for letter in letters:
        letter(fill)

def hello():
    '''draws hello world message in rainbow colors'''
    setheading(0)
    pu()
    setx(-265)
    pd()
    draw_letters(True, "red", h)
    draw_letters(True, "dark orange", e)
    draw_letters(True, "yellow", l)
    draw_letters(True, "green", l)
    draw_letters(True, "blue", o)
    pu()
    setx(xcor() + 30)
    draw_letters(True, "blue", w)
    draw_letters(True, "blue violet", o)
    draw_letters(True, "violet", r)
    draw_letters(True, "pink", l)
    draw_letters(True, "red", d)

def hola():
    '''draws hola world message in cool green color'''
    setheading(0)
    pu()
    setx(-215)
    pd()
    draw_letters(True, "green", h, o, l, a)
    pu()
    setx(xcor() + 30)
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
            tracer(False)
            for k in range(90):
                fd(1)
                rt(2)
            rt(90)
            tracer(True,10)

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
    goto(xcor()+20,ycor())
    goto(xcor(),ycor()+80)
    goto(xcor()-20,ycor())
    goto(xcor(),ycor()-80)
    ef()
    fc('dark green')
    color('dark green')
    pu()
    goto(xcor()+10,ycor()+80)
    pd()
    bf()
    circle(20)
    ef()
    goto(xcor()-20,ycor()-20)
    bf()
    circle(20)
    ef()
    pu()
    goto(xcor()+40,ycor())
    pd()
    bf()
    circle(20)
    ef()
    pu()
    goto(xcor()-30,ycor()-60)
    pd()
    color(oc[0])
    fc(oc[1])

#Setup stuff
def begin():
    '''Starts up the turtle screen and sets up the turtle object'''
    sc = Screen()
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

    speed(0)
    shape("turtle")
    fc("light blue")

def rs():
    '''moves turtle back to center clears screen and resets the turtle object'''
    reset()
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
    setx(xcor()+step)
    pd()

def mvw(step=10):
    '''moves the turtle west(left) without drawing'''
    pu()
    setx(xcor()-step)
    pd()

def mvn(step=10):
    '''moves the turtle north(up) without drawing'''
    pu()
    sety(ycor()+step)
    pd()

def mvs(step=10):
    '''moves the turtle south(down) without drawing'''
    pu()
    sety(ycor()-step)
    pd()

def mvne(step=10):
    '''moves the turtle northeast without drawing'''
    pu()
    goto(xcor()+step,ycor()+step)
    pd()

def mvnw(step=10):
    '''moves the turtle northwest without drawing'''
    pu()
    goto(xcor()-step,ycor()+step)
    pd()

def mvsw(step=10):
    '''moves the turtle southwest without drawing'''
    pu()
    goto(xcor()-step,ycor()-step)
    pd()

def mvse(step=10):
    '''moves the turtle southeast without drawing'''
    pu()
    goto(xcor()+step,ycor()-step)
    pd()

#Create some shortcut function names
cl = clear
fc = fillcolor
bf = begin_fill
ef = end_fill

if __name__ == "__main__":
    def go_up():
        '''Moves turtle up on the screen when up arrow is pressed'''
        setheading(90)
        fd(10)

    def go_right():
        '''Moves turtle right on screen when right arrow is pressed'''
        setheading(0)
        fd(10)

    def go_left():
        '''Moves turtle left on screen when left arrow is pressed'''
        setheading(180)
        fd(10)

    def go_down():
        '''Moves turtle down on screen when down arrow is pressed'''
        setheading(270)
        fd(10)

    def stampit(eks,why):
        '''moved the turtle to the position on the screen that was clicked and stamps itself'''
        pu()
        goto(eks,why)
        stamp()
        pd()

    #Global Turtle ready to... run
    begin()

    bgcolor('black')
    hello()
    getscreen().listen() #allows us to collect key events to move turtle, but window must be active window.
    onscreenclick(stampit)
    mainloop()
