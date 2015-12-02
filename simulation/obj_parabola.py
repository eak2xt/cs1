import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint
import math

################################################################

# This program demonstrates what happens if a pig was allowed to fly
# in accordance with classical mechanics -  parabolic motion. This
# simulation does not take into account any drag forces or friction
# parameters.

################################################################

# Initialize world
name = "And pigs fly!"
width = 750
height = 750
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a flying pig at that x coordinate
myimage = dw.loadImage("flying-pig-clip-art-1741857.bmp")

# state -> image (IO)
# draw the flying pig at the assigned initial conditions.
#

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state.xCoord, state.yCoord))


################################################################

# Change the y coordinate by the expression (v_y)(t) - (1/2)gt^2 + y_init and x
# by the expression x(t) + x_init. We can derive these expressions
# from the definitions of 2D projectile motion. We are assuming
# negligible drag forces. We do not have to assume negligible torque
# because the translationl motion will remain the same. However, this
# display will not show any rotation of the flying pig.
# state -> state


def updateState(state):
    state.yCoord = height - (((state.yVelocity)*(state.time) - ((0.5)*(10)*(state.time)*(state.time)) + (height - state.yInit)))
    state.xCoord = ((state.xVelocity)*(state.time) + state.xInit)
    state.time = state.time + 0.01
    return state

################################################################

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
def endState(state):
    if (state.xCoord > width or state.xCoord < 0) or (state.yCoord > height or state.yCoord < 0):
        return True
    else:
        return False


################################################################


# state -> event -> state
# Lists the r (position) vector with magnitude and direction
# on the screen.
def handleEvent(state, event):  
    if (event.type == pg.MOUSEBUTTONDOWN):
        addSq = math.pow(state.xCoord,2) + math.pow(state.yCoord,2)
        position = height - (math.sqrt(addSq))
        angle = math.atan(state.yCoord/state.xCoord)
        angleDeg = angle * (180/3.14)
        print("Your position is ", str(position), " at an angle, in degrees, of ", str(angleDeg))
        return(state)
    else:
        return(state)

################################################################

# The flying pig moves in parabolic motion. This state tuple takes value as
# (x coordinate, x component of velocity, y coordinate, y
# component of velocity, time, initial x coordinate, initial y
# coordinate) The initial x and y coordinates as well as bounds on the
# random paramenters were set so that the entire
# parabola could appear nicely on the display
#initState = (randint(100,500), randint(10,40), randint(100,500), randint(50,80), 0, 100, 350)

class State:
    xCoord = randint(100,500)
    xVelocity = randint(10,40)
    yCoord = randint(100,500)
    yVelocity = randint(50,80)
    time = 0
    xInit = 100
    yInit = 350

initState = State()

# Run the simulation no faster than 100 frames per second
frameRate = 100

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
