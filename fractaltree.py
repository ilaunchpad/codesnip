__author__ = 'rauts3'

import turtle


myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward( lineLen)
        myTurtle.right( 90)
        drawSpiral(myTurtle, lineLen-5)

#drawSpiral(myTurtle,20)

def drawFractal(myTurtle,linelen, order):
    if order == 0:
        myTurtle.forward(linelen)
    else:
        drawFractal(myTurtle,linelen/3, order-1)
        myTurtle.left(60)
        drawFractal(myTurtle,linelen/3, order-1)
        myTurtle.left(-120)
        drawFractal(myTurtle,linelen/3, order-1)
        myTurtle.left(60)
        drawFractal(myTurtle,linelen/3, order-1)

drawFractal(myTurtle, 60, 1)




