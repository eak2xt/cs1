module BoxTest

import Box
import bool
import unit

box1: Box bool
--box1 is a Box with a bool inside
box1 = (mkBox true)

box2: Box unit
--box2 is a Box with a unit inside
box2 = (mkBox mkUnit)

n: bool
n = unbox box1
-- n = unbox (mkBox box1)

