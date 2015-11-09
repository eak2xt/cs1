module fib

import nat

fib: pair nat nat -> nat
fib (mkPair O (S O)) = S O
fib (mkPair n (S n)) = (S n) + n
