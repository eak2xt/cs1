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
# The cat and dog start at random points moving in a random directions in
# both x and y directions

class newState:
    x_pos_cat = 300
    y_pos_cat = 300
    x_vel_cat = randint(-3,3)
    y_vel_cat = randint(-3,3)
    x_pos_pug = 600
    y_pos_pug = 600
    x_vel_pug = randint(-3,3)
    y_vel_pug = randint(-3,3)

initState = newState()

def updateDisplay(state):
    dw.fill(color)
    dw.draw(catimage, (state.x_pos_cat, state.y_pos_cat))
    dw.draw(pugimage, (state.x_pos_pug, state.y_pos_pug))


################################################################

# Change all positions by their respective velocities. If the pug hits
# the wall, generate a new velocity in the opposite direction of the
# wall it just hit.
# 
# state -> state
def updateState(state):
    if (state.x_pos_pug > 622):
        newState5s = randint(-3,-1)
        return(state.x_pos_cat+state.x_vel_cat,state.x_vel_cat,state.y_pos_cat+state.y_vel_cat,state.y_vel_cat,state.x_pos_pug+newState5s,newState5s,state.y_pos_pug+state.y_vel_pug,state.y_vel_pug)
    if (state.y_pos_pug > 622):
        newState7s = randint(-3,-1)
        return(state.x_pos_cat+state.x_vel_cat,state.x_vel_cat,state.y_pos_cat+state.y_vel_cat,state.y_vel_cat,state.x_pos_pug+state.x_vel_pug,state.x_vel_pug,state.y_pos_pug+newState7s,newState7s)
    if (state.x_pos_pug < 0):
        newState5ss = randint(1,3)
        return(state.x_pos_cat+state.x_vel_cat,state.x_vel_cat,state.y_pos_cat+state.y_vel_cat,state.y_vel_cat,state.x_pos_pug+newState5ss,newState5ss,state.y_pos_pug+state.y_vel_pug,state.y_vel_pug)
    if (state.y_pos_pug < 0):
        newState7ss = randint(1,3)
        return(state.x_pos_cat+state.x_vel_cat,state.x_vel_cat,state.y_pos_cat+state.y_vel_cat,state.y_vel_cat,state.x_pos_pug+state.x_vel_pug,state.x_vel_pug,state.y_pos_pug+newState7ss,newState7ss)
    return((state.x_pos_cat+state.x_vel_cat,state.x_vel_cat,state.y_pos_cat+state.y_vel_cat,state.y_vel_cat,state.x_pos_pug+state.x_vel_pug,state.x_vel_pug,state.y_pos_pug+state.y_vel_pug,state.y_vel_pug))

################################################################

# Terminate the simulation when the x coord or y coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# or height, or when the cat and the pug collide.
# state -> bool
def endState(state):
    if ((state.x_pos_cat > 622 or state.x_pos_cat < 0) or (state.y_pos_cat > 622 or state.y_pos_cat < 0)) or (((state.x_pos_pug <= state.x_pos_cat <= state.x_pos_pug + 128) and (state.y_pos_cat-128 <= state.y_pos_pug <= state.y_pos_cat + 128)) or ((state.y_pos_pug <= state.y_pos_cat <= state.y_pos_pug + 128) and (state.x_pos_cat-128 <= state.x_pos_pug <= state.x_pos_cat + 128)) or ((state.x_pos_pug <= state.x_pos_cat + 128 <= state.x_pos_pug + 128) and (state.y_pos_cat-128 <= state.y_pos_pug <= state.y_pos_cat + 128)) or ((state.y_pos_pug <= state.y_pos_cat + 128 <= state.y_pos_pug + 128) and (state.x_pos_cat-128 <= state.x_pos_pug <= state.x_pos_cat + 128))):
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
        return(state.x_pos_cat,newState1,state.y_pos_cat,newState3,state.x_pos_pug,newState5,state.y_pos_pug,newState7)
    else:
        return(state)
    

################################################################

# World state will be image at random point

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
