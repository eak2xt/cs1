module colors

import pair

data primary = red | yellow | blue
data mixed = dred | dyellow | dblue | violet | green | orange

f: pair primary primary -> mixed
f(mkPair red blue) = violet
