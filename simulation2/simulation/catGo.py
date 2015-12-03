# from trepan.api import debug

# import pdb
# pdb.set_trace()

import runWorld as rw
import drawWorld as dw


# Initialize world
name = "Cat Go!"
width = 500
height = 500
rw.newDisplay(width, height, name)

# World state will be single x coordinate at left edge of world
initState = 0

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")

# Type state -> image
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state[0], height/2))


# We'll update the state on each tick by incrementing the x stateinate

#Type state -> state
def updateState(state):
    return((state[0]+state[1]), state[1])

# We'll terminate when the x stateinate reaches the screen edge

# Type state -> bool
def endState(state):
    if (state[0] >= width):
        return True
    else:
        return False


# For now we'll handle events just logging them to the console
#Type state -> event -> state (addresses any new event - click, etc to
#move cat to the opposite direction)
def handleEvent(state, event):
    print(event)
    return((state[0],-1)

# Off we go! Start the cat at the left edge, and try for 30 FPS 
frameRate = 60
initState = (0,1)
#represents x and delta x
# debug()
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
