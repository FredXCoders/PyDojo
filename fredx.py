'''
FredX - python tutorial module for the FredX CodeDojo.

  This module handles the setup process of the turtle module to minimize typing for beginners.
  Letter functions have been defined to print "HELLO WORLD" graphically on the screen.  Additional fun
  shapes and designs have been added to allow the kids to create some cool effects by stringing them together.

  if module is run it will print Hello World message in colors and arrow keys will move the turtle around once
  the window is active (by clicking it).  The q key will quit the program.

  to use this module for coding use the "from fredx import *" to import the module contents into the namespace.  several
  functions have been re-defined to reduce typing and importing this way allows them to be used without pre-pending the
  "fredx." module name.
'''
import turtle

__author__ = "sabadam32"
__version__ = '1.0'

# Only define key functions if this is being run as a program.
if __name__ == "__main__":
    def go_up():
        '''Moves turtle up on the screen when up arrow is pressed'''
        __turtle__.setheading(90)
        fd(10)

    def go_right():
        '''Moves turtle right on screen when right arrow is pressed'''
        __turtle__.setheading(0)
        fd(10)

    def go_left():
        '''Moves turtle left on screen when left arrow is pressed'''
        __turtle__.setheading(180)
        fd(10)

    def go_down():
        '''Moves turtle down on screen when down arrow is pressed'''
        __turtle__.setheading(270)
        fd(10)

# Letters are all designed to fit 40 W x 110 H with a 10 W space after the letter making the total width 50
def h(fill=False):
    '''draws a capital H.
     This is a DOCstring, which is a special comment that DOCuments our code.  When you type help() in python it
     displays these strings.  Don't take my word for it... try it yourself!'''
    if fill: __turtle__.begin_fill()
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
    if fill: __turtle__.end_fill()  # single statement 'if' can be put on the same line
    pu()
    fd(50)
    pd()

def e(fill=False):
    '''draws a capital E.  Docstrings need to be the first line in a function definition'''
    if fill: __turtle__.begin_fill()
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
    if fill: __turtle__.end_fill()
    pu()
    fd(50)
    pd()

def l(fill=False):
    '''draws a capital L.  Doctrings must use the multi-line comment format.'''
    if fill: __turtle__.begin_fill()
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
    if fill: __turtle__.end_fill()
    pu()
    fd(50)
    pd()

def o(fill=False):
    '''draws a capital O'''
    pu()
    fd(20)
    pd()
    if fill: __turtle__.begin_fill()
    circle(20, 90)
    fd(70)
    circle(20, 180)
    fd(70)
    circle(20, 90)
    if fill: __turtle__.end_fill()
    pu()
    __turtle__.sety(gy() + 10)
    pd()
    fc = __turtle__.fillcolor()
    __turtle__.fillcolor(__turtle__.getscreen().bgcolor())
    __turtle__.begin_fill()
    circle(10, 90)
    fd(70)
    circle(10, 180)
    fd(70)
    circle(10, 90)
    __turtle__.end_fill()
    pu()
    __turtle__.goto(gx() + 30, gy() - 10)
    pd()
    __turtle__.fillcolor(fc)

def w(fill=False):
    '''draws a capital W.'''
    pu()
    __turtle__.sety(gy() + 110)
    pd()
    if fill: __turtle__.begin_fill()
    __turtle__.goto(gx() + 10, gy() - 110)
    __turtle__.goto(gx() + 5, gy())
    __turtle__.goto(gx() + 5, gy() + 50)
    __turtle__.goto(gx() + 5, gy() - 50)
    __turtle__.goto(gx() + 5, gy())
    __turtle__.goto(gx() + 10, gy() + 110)
    __turtle__.goto(gx() - 10, gy())
    __turtle__.goto(gx() - 5, gy() - 55)
    __turtle__.goto(gx() - 2, gy() + 20)
    __turtle__.goto(gx() - 6, gy())
    __turtle__.goto(gx() - 2, gy() - 20)
    __turtle__.goto(gx() - 5, gy() + 55)
    __turtle__.goto(gx() - 10, gy())
    if fill: __turtle__.end_fill()
    pu()
    __turtle__.goto(gx() + 50, gy() - 110)
    pd()

def r(fill=False):
    '''draws a capital R.'''
    if fill: __turtle__.begin_fill()
    fd(10)
    lt(90)
    fd(50)
    rt(90)
    __turtle__.goto(gx() + 20, gy() - 50)
    fd(10)
    __turtle__.goto(gx() - 20, gy() + 50)
    circle(20, 90)
    fd(20)
    circle(20, 90)
    fd(20)
    lt(90)
    fd(110)
    if fill: __turtle__.end_fill()
    pu()
    __turtle__.goto(gx() + 10, gy() + 60)
    pd()
    lt(90)
    fc = __turtle__.fillcolor()
    __turtle__.fillcolor(__turtle__.getscreen().bgcolor())
    __turtle__.begin_fill()
    fd(10)
    circle(10, 90)
    fd(20)
    circle(10, 90)
    fd(10)
    lt(90)
    fd(40)
    __turtle__.end_fill()
    __turtle__.fillcolor(fc)
    lt(90)
    pu()
    __turtle__.goto(gx() + 40, gy() - 60)
    pd()

def d(fill=False):
    '''draws a capital D'''
    if fill: __turtle__.begin_fill()
    fd(20)
    circle(20, 90)
    fd(70)
    circle(20, 90)
    fd(20)
    lt(90)
    fd(110)
    lt(90)
    if fill: __turtle__.end_fill()
    pu()
    __turtle__.goto(gx() + 10, gy() + 10)
    pd()
    fc = __turtle__.fillcolor()
    __turtle__.fillcolor(__turtle__.getscreen().bgcolor())
    __turtle__.begin_fill()
    fd(10)
    circle(10, 90)
    fd(70)
    circle(10, 90)
    fd(10)
    lt(90)
    fd(90)
    __turtle__.end_fill()
    lt(90)
    pu()
    __turtle__.goto(gx() + 40, gy() - 10)
    pd()
    __turtle__.fillcolor(fc)

def draw_letters(fill=False, color=None, *letters):
    '''Draws a series of letters'''
    if fill: __turtle__.fillcolor(color)
    for letter in letters:
        __turtle__.fillcolor(color)
        letter(True)

def hello_world_rainbow():
    '''draws hello world message in rainbow colors'''
    pu()
    sx(-265)
    pd()
    draw_letters(True, "red", h)
    draw_letters(True, "dark orange", e)
    draw_letters(True, "yellow", l)
    draw_letters(True, "green", l)
    draw_letters(True, "blue", o)
    pu()
    sx(gx() + 30)
    draw_letters(True, "blue", w)
    draw_letters(True, "blue violet", o)
    draw_letters(True, "violet", r)
    draw_letters(True, "pink", l)
    draw_letters(True, "red", d)

def hello_world():
    '''draws hello world message in cool green color'''
    pu()
    sx(-265)
    pd()
    draw_letters(True, "green", *[h, e, l, l, o])
    pu()
    sx(gx() + 30)
    draw_letters(True, "green", *[w, o, r, l, d])

# Shapes
def square(size=100):
    '''draws a square'''
    rt(45)
    circle(size,steps=4)
    lt(45)

def hexagon(size=100):
    '''draws a hexagon'''
    rt(30)
    circle(size,steps=6)
    lt(30)

def octagon(size=100):
    '''draws an octagon'''
    rt(22.5)
    circle(size,steps=8)
    lt(22.5)

def flower():
    '''Draws a flower like thing on the screen'''
    for i in range(8):
        rt(45)

        for j in range(6):
            __turtle__.tracer(False)
            for k in range(90):
                fd(1)
                rt(2)
            rt(90)
            __turtle__.tracer(True,10)

def star():
    '''Draws a star'''
    for i in range(17):
        fd(100)
        lt(150)
        if abs(__turtle__.pos()) < 1:
            break

#Setup stuff
def begin():
    '''Starts up the turtle screen and sets up the turtle.'''
    sc = turtle.Screen()
    sc._root.attributes("-topmost", 1)  # hack to get the window to show in front of the terminal

    if __name__ == "__main__":
        sc.setup(1.0, 1.0)  # make screen full window
        sc.onkey(go_up, "Up")
        sc.onkey(go_down, "Down")
        sc.onkey(go_left, "Left")
        sc.onkey(go_right, "Right")
        sc.onkey(quit, "q")

    yertle = turtle.Turtle()
    yertle.speed(0)
    yertle.shape("turtle")
    yertle.fillcolor("red")
    return yertle

#Global Turtle ready to... run
__turtle__ = begin()

# Redefine functions for minimal typing
pu = __turtle__.pu  # Pen Up (Doesn't draw when it moves)
pd = __turtle__.pd  # Pen Down (Draws as it moves)
lt = __turtle__.lt  # Left Turn (Specify degrees counter-clockwise)
rt = __turtle__.rt  # Right Turn (Specify degrees clockwise)
fd = __turtle__.fd  # Forward (Specify steps)
bk = __turtle__.bk  # Backward (Specify steps)
rs = __turtle__.reset  # Reset (Moves Turtle back to center of screen)
cl = __turtle__.clear  # Clear (Clears the screen of all current drawings and moves Turtle back to center of screen)
ht = __turtle__.ht  # Hide Turtle (Turtle does not show on screen)
st = __turtle__.st  # Show Turtle (Turtle appears on screen)
sx = __turtle__.setx  # Sets the x coordinate of the Turtle (Moves it left and right)
sy = __turtle__.sety  # Sets the y coordinate of the Turtle (Moves it up and down)
circle = __turtle__.circle  # Draws a circle
gx = __turtle__.xcor  # Gets the x coordinate of the Turtle
gy = __turtle__.ycor  # Gets the y coordinate of the Turtle
pos = __turtle__.pos() # Gets the Turtle position

if __name__ == "__main__":
    hello_world_rainbow()
    __turtle__.getscreen().listen() #allows us to collect key events to move turtle, but window must be active window.
    turtle.mainloop()