module listTest

import list
import bool
import nat
import eq
import Serialize

l1: list nat
l1 = nil

l2: list nat
l2 = (S O) :: O :: nil

l3: list nat
l3 = (S O) :: (S (S O)) :: (S (S (S O))) :: nil

|||takes a pair of lists and returns the list made by appending the lists
append: list a -> list a -> list a
append nil l = l
append (h::t) l = h::(append t l)

la: list nat
la = nil

lb: list nat
lb = O :: nil

lc: list nat
lc = (S O) :: (S (S O)) :: nil

ld: list nat
ld = (S O) :: (S (S O)) :: (S (S (S O))) :: nil

lengthla: nat
lengthla = length la

lengthld: nat
lengthld = length ld
---expects 3

lengthlb: nat
lengthlb = length lb
--expects 1

appendlcld: list nat
appendlcld = append lc ld
--expects (1, 2, 1, 2, 3, nil)

appendlald: list nat
appendlald = append la ld
-- expects (1, 2, 3, nil)module listTest

mapevenbtest: list bool
mapevenbtest = map evenb (O::(S O)::(S (S O))::(S (S (S (S O))))::nil)

filterevenbtest: list nat
filterevenbtest = filter evenb (O::(S O)::(S (S O))::(S (S (S (S O))))::nil)

isThree: bool
isThree = (member (S (S (S O))) l2)

s: String
s = toString l2
