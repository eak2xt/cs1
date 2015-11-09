module ite

import bool

||| if then else expression
||| if bool is true I return the first one
||| otherwise I return the second one
ite: bool -> a -> a -> a
ite true tb fb = tb
ite false tb fb = fb
