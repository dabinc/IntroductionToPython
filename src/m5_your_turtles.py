"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Dabin
"""
########################################################################
# Done
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg
Dabin=rg.SimpleTurtle('turtle')

Dabin.pen=rg.Pen('red',15)
a=100
b=350

for k in range(3):
    Dabin.pen_up()
    Dabin.left(90)
    Dabin.forward(100)
    Dabin.right(90)
    Dabin.pen_down()
    Dabin.left(-45)
    Dabin.backward(a)
    Dabin.left(45)
    Dabin.backward(a)
    Dabin.left(45)
    Dabin.backward(a)
    Dabin.left(45)
    Dabin.backward(a)
    Dabin.left(45)
    Dabin.backward(b)
    Dabin.left(90)
    Dabin.backward(b)
    Dabin.left(45)
    Dabin.backward(a)
    Dabin.left(45)
    Dabin.backward(a)
    Dabin.left(45)
    Dabin.backward(a)
    Dabin.left(45)
    Dabin.backward(a)
    a=a-20
    b=b-70


