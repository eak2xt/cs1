module Person

import bool

||| A record type that is equivalent to:
||| (data Person = mkPerson String nat)
||| but where we give names to fields.
||| A person has a name and an age in
||| years.
record Person where
  constructor mkPerson
  name: String
  age: Nat
  height: Nat
  gender: bool

getName': Person -> String
getName' (mkPerson name age height gender) = name

getHeight': Person -> Nat
getHeight' (mkPerson name age height gender) = height

--field override functions ("setters")

setName': Person -> String -> Person
setName' p n = record { name = n } p

setAge': Person -> Nat -> Person
setAge' p a = record { age = a } p

setHeight': Person -> Nat -> Person
setHeight' p h = record { height = h } p

setGender': Person -> bool -> Person
setGender' p g = record { gender = g } p
