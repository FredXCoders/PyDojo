PyDojo
======
This repo is for the FredX CoderDojo python modules.

fredx.py is a simple tutorial module that will allow the kids to do some basic things with minimal typing.
The following functions have been defined:

Shapes:
 - circle, square, rectangle, triangle, hexagon, octagon, star, flower, house, tree.
 - loops - draws a shape as the turtle spins around the center point

Movement:
 - Based on the current direction of the turtle:
   + mvf (forward), mvb (backward), mvl (left), mvr (right), mvlb (diagonal left and back),
     mvlf (diagonal left and forward), mvrf (diagonal right and forward), mvrb (diagonal right and back)
 - Based on the screen coordinates:
   + mvn (north), mvs (south), mvw (west), mve (east), mvnw (diagonal north west), mvne (diagonal north east),
     mvse (diagonal south east), mvsw (disgonal south west)

Setup:
 - begin - sets everything up and configures the turtle for use.
 - rs - resets everything.  Clears the screen (creates it again if the window was closed) and sets up the turtle again.

Shortcuts:
 - cl (clear), fc (fillcolor), bf (begin_fill), ef (end_fill)

Letters:
 - h, e, l, o, w, r, d, a - all these draw a letter on the screen
 - draw_letters, hello, hola - these help draw the letters


guess.py is a simple number guessing game that will allow the kids to see how variables, loops, and branching work.

secretCode.py is a simple message encoder and decoder.
