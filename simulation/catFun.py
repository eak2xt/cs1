import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint
import time

################################################################

# This program is an interactive simulation/game. A cat and a dog start
# to move across the screen. The directions of movement are reversed
# on each "mouse down" event.
#
# The program also generates a new color for the background every time
# it runs.
#
# The state of the program is represented by a tuple (cx-pos,
# delta-cx-pos, cy-pos, delta-xy-pos, dx-pos, delta-dx-pos, dy-pos, delta-dy-pos).
# The first element, cx-pos, represents the x-coordinate of the cat.
# The second element, delta-cx-pos, represents the amount that the
# position changes on each iteration of the simulation loop. The third
# element represents the y-coordinate of the cat, and so on.
# 
# Pressing a mouse button down while this simulation run updates the state
# by leaving all positions changed but generating a new velocity for
# each position from the range (-3, 3). That is, each mouse-click will
# make both the cat and dog change direction.
#
# The simulation ends when the cat is allowed to reach either the left
# or the right edge of the screen, or when it collides the dog. When
# the dog touches the edge of the screen, the program will generate a
# new x or y velocity that sends it in the opposite direction of the
# wall it hit.
#
# The goal of the game is to keep Grumpy Cat alive by avoiding both
# the sides of the screen and the dog!

################################################################

# Initialize world
name = "Colorific Cat & Dog Fun!"
width = 750
height = 750
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat and a dog at their designated coordinates
catimage = dw.loadImage("grumpycat.bmp")
pugimage = dw.loadImage("pug.bmp")
color = (randint(0,255), randint(0,255), randint(0,255))
start = time.time()

# state -> image (IO)
# draw the cat and the dog at the points determined by the state tuple
#
def updateDisplay(state):
    dw.fill(color)
    dw.draw(catimage, (state[0], state[2]))
    dw.draw(pugimage, (state[4], state[6]))


################################################################

# Change all positions by their respective velocities. If the pug hits
# the wall, generate a new velocity in the opposite direction of the
# wall it just hit.
# 
# state -> state
def updateState(state):
    if (state[4] > 622):
        newState5s = randint(-3,-1)
        return(state[0]+state[1],state[1],state[2]+state[3],state[3],state[4]+newState5s,newState5s,state[6]+state[7],state[7])
    if (state[6] > 622):
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
# or height, or when the cat and the pug collide.
# state -> bool
def endState(state):
    if ((state[0] > 622 or state[0] < 0) or (state[2] > 622 or state[2] < 0)) or (((state[4] <= state[0] <= state[4] + 128) and (state[2]-128 <= state[6] <= state[2] + 128)) or ((state[6] <= state[2] <= state[6] + 128) and (state[0]-128 <= state[4] <= state[0] + 128)) or ((state[4] <= state[0] + 128 <= state[4] + 128) and (state[2]-128 <= state[6] <= state[2] + 128)) or ((state[6] <= state[2] + 128 <= state[6] + 128) and (state[0]-128 <= state[4] <= state[0] + 128))):
        stop = time.time()
        print("You only let Grumpy Cat survive for", stop-start, "seconds?")
        return True
    else:
        return False

################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat's
# and dog's direction. The game is to keep the cat alive by not letting it run off the
# edge of the screen or into the pug.
#
# state -> event -> state
#
def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        newState1 = randint(-3,3)
        newState3 = randint(-3,3)
        newState5 = randint(-3,3)
        newState7 = randint(-3,3)
        return(state[0],newState1,state[2],newState3,state[4],newState5,state[6],newState7)
    else:
        return(state)
    

################################################################

# World state will be image at random point

# The cat and dog start at random points moving in a random directions in
# both x and y directions
initState = (300,(randint(-3,3)),300,(randint(-3,3)),600,(randint(-3, 3)), 600, (randint(-3,3)))

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
