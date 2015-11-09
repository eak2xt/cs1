module apple

import relation
import bool
import list

record apple where
  constructor mkApple
  type: String
  amount: Nat
  ripe: bool

types': String
types' = query2 apple amount ripe (++) ""

amount': Nat
amount' = query2 apple amount ripe countOne plus 0

ripe': bool
ripe' = query2 apple amount ripe (++) ""
