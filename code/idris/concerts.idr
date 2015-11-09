module concerts

import bool

||| A record type that is equivalent to:
||| (data Person = mkConcert String Nat Nat)
||| but where we give names to fields.
||| A band has a band name, an audience count,
||| and whether it is sold out or not.

record concerts where
       constructor MkConcert
       band: String
       audience: Nat
       soldout: bool
       opener: bool

str: concerts
str = MkConcert "The Strokes" 300 true true

koo: concerts
koo = MkConcert "The Kooks" 200 false true

od: concerts
od = MkConcert "One Direction" 500 true true

dmb: concerts
dmb = MkConcert "David Matthews Band" 100 false false

