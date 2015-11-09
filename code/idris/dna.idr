module dna

import list
import pair

data base = A | C | G | T

complement_base: base -> base
complement_base A = T
complement_base T = A
complement_base C = G
complement_base G = C

complement_strand: list base -> list base
complement_strand (h::t) = map complement_base (h::t)

strand1: list (pair base base) -> list base
strand1 nil = nil
strand1 ((mkPair x y)::nil) = x::nil
strand1 ((mkPair w x)::(mkPair y z)::t) = w::y::strand1 t

strand2: list (pair base base) -> list base
strand2 nil = nil
strand2 ((mkPair x y)::nil) = y::nil
strand2 ((mkPair w x)::(mkPair y z)::t) = x::z::strand2 t

getPair: base -> pair base base
getPair n = (mkPair n (complement_base n))

complete: list base -> list (pair base base)
complete n = map getPair n

baseNat: base -> base -> Nat
baseNat A A = 1
baseNat T T = 1
baseNat C C = 1
baseNat G G = 1
baseNat _ _ = 0

countBase: list base -> base -> Nat
countBase l x = list.foldr plus 0 (map (baseNat x) l)

