module list

import nat
import bool
import ite
import eq
import Serialize

infixr 7 ::,++

data list a = nil | (::) a (list a)

length: list a -> nat
length nil = O
length (h::t) = S (length t)

(++): list a -> list a -> list a
(++) nil l2 = l2
(++) (h::t) l2 = h::(t++l2)

|||map a function over the elements of a list
map: (a -> b) -> list a -> list b
map f nil = nil
map f (h::t) = (f h)::(map f t)

||| give a list and a predicate on elements
||| return the sublist of elements for which
||| the predicate is true
filter: (a -> bool) -> list a -> list a
filter f nil = nil
filter f (h::t) = ite (f h)
                      (h::(filter f t))
                          (filter f t)
foldr: (a -> a -> a) -> a -> list a -> a
foldr f id nil = id
foldr f id (h::t) = f h (list.foldr f id t)

--eql: a -> a -> bool
--eql v1 v2 = ?big_hole

member: (eq a) => a -> list a -> bool
member v nil = false
member v (h::t) = ite (eql v h) true (member v t)

not_member: (eq a) => a -> a -> bool
not_member a1 a2 = not (eql a1 a2)

filter_member: (eq a) => list a -> list a -> list a
filter_member l1 nil = l1
filter_member (h::t) l2 = ite (member h l2)(filter_member t l2)(h::(filter_member t l2))

filter_notmember: (eq a) => list a -> list a -> list a
filter_notmember l1 nil = nil
filter_notmember (h::t) l2 = ite (member h l2)(h::filter_member t l2)(filter_member t l2)

combine: (eq a) => list a -> list a -> list a
combine l1 nil = l1
combine l1 l2 = (filter_member l1 l2)++l2

instance (eq a) => eq (list a) where
  eql nil nil = true
  eql (h::t) nil = false
  eql nil (h::t) = false
  eql (h1::t1) (h2::t2) =
    and (eql h1 h2) (eql t1 t2)

toStringList: (Serialize a) => list a -> String
toStringList nil = ""
toStringList (h::nil) = (toString h)
toStringList (h::t) = (toString h) ++ ", " ++ (toStringList t)

instance (Serialize a) => Serialize (list a) where
  toString l = "[" ++ (toStringList l) ++ "]"
