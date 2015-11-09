module unitTest

import unit
import Serialize

u: unit
u = mkUnit

v: unit
v = mkUnit

u1: unit
u1 = mkUnit

u2: unit
u2 = mkUnit

u3: unit
u3 = id_unit mkUnit

s: String
s = toString u1
