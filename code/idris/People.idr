module People

import Person
import list
import bool

tom: Person
tom = mkPerson "Tom" 19 56 false

mary: Person
mary = mkPerson "Mary" 20 59 true

ge: Person
ge = mkPerson "Ge" 21 64 true

daryl: Person
daryl = mkPerson "Daryl" 19 71 false

people: list Person
people = tom::mary::ge::daryl::nil

map: (a -> b) -> list a -> list b
map f nil = nil
map f (h::t) = (f h)::(list.map f t)

ages: list Nat
ages = list.map age people

names: list String
names = list.map name people
