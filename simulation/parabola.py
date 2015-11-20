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

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("flying-pig-clip-art-1741857.bmp")

# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple
#


def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state[0], state[2]))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state


def updateState(state):
    yCord = height - (((state[3])*(state[4])) - ((0.5)*(10)*(state[4])*(state[4])) + (height - state[6]))
    xCord = ((state[1])*(state[4]) + state[5])
    time = state[4] + 0.01
    return((xCord, state[1], yCord, state[3], time, state[5], state[6]))

################################################################

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
def endState(state):
    if (state[0] > width or state[0] < 0) or (state[2] > height or state[2] < 0):
        return True
    else:
        return False


################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat
# direction. The game is to keep the cat alive by not letting it run off the
# edge of the screen.
#
# state -> event -> state
# Stops the simulation and lists the physical parameters in question
# on the screen.
def handleEvent(state, event):  
    if (event.type == pg.MOUSEBUTTONDOWN):
        print("Your y velocity is " + state)
        return((900, state[1], 900, state[3], state[4], state[5], state[6]))
    else:
        return(state)

################################################################

# World state will be single x coordinate at left edge of world

# The cat moves in parabolic motion.
initState = (100, 20, 500, 75, 0, 100, 600)

# Run the simulation no faster than 60 frames per second
frameRate = 100

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
