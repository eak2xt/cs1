module nextColor

data Color = red | green | amber

nextColor: Color -> Color
nextColor red = green
nextColor green = amber
nextColor amber = red

