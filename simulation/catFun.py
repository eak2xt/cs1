import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

################################################################

# This program is an interactive simulation/game. A cat starts
# to move across the screen. The direction of movement is reversed
# on each "mouse down" event.
#
# The state of the cat is represented by a tuple (pos, delta-pos).
# The first element, pos, represents the x-coordinate of the cat.
# The second element, delta-pos, represents the amount that the
# position changes on each iteration of the simulation loop.
#
# For example, the tuple (7,1) would represent the cat at x-coord,
# 7, and moving to the right by 1 pixel per "clock tick."
# 
# The initial state of the cat in this program is (0,1), meaning that the cat
# starts at the left of the screen and moves right one pixel per tick.
#
# Pressing a mouse button down while this simulation run updates the cat state
# by leaving pos unchanged but reversing delta-pos (changing 1 to -1 and vice
# versa). That is, pressing a mouse key reverses the direction of the
# cat.
#
# The simulation ends when the cat is allowed to reach either the left
# or the right edge of the screen.

################################################################

# Initialize world
name = "Colorific Cat & Dog Fun!"
width = 500
height = 500
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
catimage = dw.loadImage("cat.bmp")
pugimage = dw.loadImage("pug.bmp")
color = (randint(0,255), randint(0,255), randint(0,255))


# state -> image (IO)
# draw the cat at a point determined by the state tuple
#
def updateDisplay(state):
    dw.fill(color)
    dw.draw(catimage, (state[0], state[2]))
    dw.draw(pugimage, (state[4], state[6]))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):
    if (state[4] > 370):
        newState5s = randint(-3,-1)
        return(state[0]+state[1],state[1],state[2]+state[3],state[3],state[4]+newState5s,newState5s,state[6]+state[7],state[7])
    if (state[6] > 370):
        newState7s = randint(-3,-1)
        return(state[0]+state[1],state[1],state[2]+state[3],state[3],state[4]+state[5],state[5],state[6]+newState7s,newState7s)
    if (state[4] < 0):
        newState5ss = randint(1,3)
        return(state[0]+state[1],state[1],state[2]+state[3],state[3],state[4]+newState5ss,newState5ss,state[6]+state[7],state[7])
    if (state[6] < 0):
        newState7ss = randint(1,3)
        return(state[0]+state[1],state[1],state[2]+state[3],state[3],state[4]+state[5],state[5],state[6]+newState7ss,newState7ss)
    return((state[0]+state[1],state[1],state[2]+state[3],state[3],state[4]+state[5],state[5],state[6]+state[7],state[7]))

################################################################

# Terminate the simulation when the x coord or y coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# or height
# state -> bool
def endState(state):
    if ((state[0] > 400 or state[0] < 0) or (state[2] > 400 or state[2] < 0)):
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
#
def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        r = (randint(0, 255))
        g = (randint(0, 255))
        b = (randint(0, 255))
        color = (r, g, b)
        newState1 = randint(-3,3)
        newState3 = randint(-3,3)
        newState5 = randint(-3,3)
        newState7 = randint(-3,3)
        return(state[0],newState1,state[2],newState3,state[4],newState5,state[6],newState7)
    else:
        return(state)
    

################################################################

# World state will be image at random point

# The cat starts at a random point moving in a random direction in
# both x and y directions
initState = (200,(randint(-3,3)),200,(randint(-3,3)),300,(randint(-3, 3)), 300, (randint(-3,3)))

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
