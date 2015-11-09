module nat

import bool
import pair
import eq
import Serialize

data nat = O | S nat

||| returns true if the argument is (represents) zero, otherwise false
isZero: nat -> bool
isZero O = true
isZero _ = false

||| Returns the successor of any given nat
succ: nat -> nat
succ n = S n

||| returns the predecessor of any given nat
pred: nat -> nat
pred O = O
pred (S n) = n

||| return true if the argument is even otherwise false
evenb: nat -> bool
evenb O = true
evenb (S O) = false
evenb (S (S n)) = evenb n

add: nat -> nat -> nat
add O m = m
add (S n) m = S (add n m)

mult: nat -> nat -> nat
mult O m = O
mult (S n) m = add m (mult n m)

fact: nat -> nat
fact O = (S O)
fact (S n') = mult (S n') (fact n')

sub: nat -> nat -> nat
sub O m = O
sub n O = n
sub (S n) (S m) = sub n m

le: nat -> nat -> bool
le O m = true
le (S n) O = false
le (S n) (S m) = le n m

exp: nat -> nat -> nat
exp x O = S O
exp x (S n) = mult x (exp x n)

eql_nat: nat -> nat -> bool
eql_nat O O = true
eql_nat O m = false
eql_nat (S n) O = false
eql_nat (S n) (S m) = eql_nat n m

gt: nat -> nat -> bool
gt O O = false
gt m O = false
gt (S n) O = true
gt (S n) (S m) = gt n m

ge: nat -> nat -> bool
ge O O = false
ge O (S m) = false
ge (S n) O = true
ge (S n) (S m) = ge n m

lt: nat -> nat -> bool
lt O O = false
lt O (S m) = true
lt (S n) O = false
lt (S n) (S m) = lt n m

fib: nat -> nat
fib O = O
fib (S O) = S O
fib (S (S n)) = add (fib (S n)) (fib n)

instance eq nat where
  eql n1 n2 = eql_nat n1 n2

instance Serialize nat where
  toString O = "Z"
  toString (S n) = "|" ++ (toString n)
