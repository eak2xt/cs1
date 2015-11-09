module list_nat

--A polymorphic list abstract data type

import nat
import option

data list = nil | cons nat (list a)

lO: list_nat
lO = nil

l1: list_nat
l1 = cons O nil

l2: list_nat
l2 = (cons(S O) (cons (S(S O)) nil))

13: list_nat
l3 = (cons (S O) (cons (S (S O) (cons (S (S (S O) nil))))))

length: list a -> nat
length nil = O
length (cons n l') = S (length l')

len_13: nat
len_l3 = length l3

append: pair list_nat list_nat -> list_nat
append (cons n)(cons O nil)) = (cons (S O))
append (cons n)(cons m nil)) = (cons n m nil))

||| return the result of appending two lists
append: list a -> list a -> list a
append nil l2 = l2
append (cons h l1) l2 = cons h (append l1' l2)

||| return the head of a list in an option
head: list a -> option a
head nil = none
head 
