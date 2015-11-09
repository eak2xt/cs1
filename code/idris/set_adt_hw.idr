module set_spec

import bool
import option
import pair
import list
import nat
import eq
import Serialize
import list
import ite

data set: (a: Type) -> Type

emptySet: set a

isEmpty: (s: set a) -> bool

set_insert: (eq a) => (v: a) -> (s: set a) -> set a

set_remove: (eq a) => (v: a) -> (s: set a) -> set a

set_cardinality: (s: set a) -> nat

set_member: (eq a) => (v: a) -> (s: set a) -> bool

set_union: (eq a) => (s1: set a) -> (s2: set a) -> set a

set_intersection: (eq a) => (s1: set a) -> (s2: set a) -> set a

set_difference: (eq a) => (s1: set a) -> (s2: set a) -> set a

set_forall: (p: a -> bool) -> (s: set a) -> bool

set_exists: (p: a -> bool) -> (s: set a) -> bool

set_witness: (p: a -> bool) -> (s: set a) -> option a

set_product: (s1: set a) -> (s2: set b) -> set (pair a b)

set_powerset: (s: set a) -> set (set a)

set_eql: (eq a) => (s1: set a) -> (s2: set a) -> bool

set_toString: (Serialize a) => set a -> String

instance (eq a) => eq (set a) where
  eql s1 s2 = set_eql s1 s2

instance (Serialize a) => Serialize (set a) where
  toString s = set_toString s

data set a = mkSet (list a)

emptySet = mkSet nil

isEmpty (mkSet nil) = true
isEmpty _ = false

set_insert v (mkSet l) = ite (member v l)
                             (mkSet l)
                             (mkSet (v::l))

list_remove: (eq a) => (v: a) -> (l: list a) -> list a
list_remove v l = filter (not_member v) l

set_remove v (mkSet l) = mkSet (list_remove v l)

set_cardinality (mkSet l) = length l

set_member v (mkSet l) = (member v l)

set_union (mkSet l1) (mkSet l2) = mkSet(combine l1 l2)

intersect: (eq a) => list a -> list a -> list a
intersect nil _ = nil
intersect (h::t) l2 = ite (member h l2)
                    (h::(intersect t l2))
                    (intersect t l2)

set_intersection (mkSet l1) (mkSet l2) = mkSet (intersect l1 l2)

list_difference: (eq a) => list a -> list a -> list a
list_difference nil _ = nil
list_difference h nil = h
list_difference (h::t) l2 = ite (member h l2)
                            (list_difference t l2)
                            (h::(list_difference t l2))

set_difference (mkSet l1) (mkSet l2) = mkSet (list_difference l1 l2)

set_forall p (mkSet l) = eql nil (filter p l)

set_exists p (mkSet l) = not (eql nil (filter p l))

list_witness: (p: a -> bool) -> (s: list a) -> option a
list_witness p nil = none
list_witness p (h::t) = ite (p h)
                      (some h)
                      (list_witness p t)

set_witness p (mkSet l) = list_witness p l

help1: a -> list b -> list (pair a b)
help1 a nil = nil
help1 a (h::t) = ((mkPair a h)::(help1 a t))

|||takes two lists and returns a list of all pairs
help2: list a  -> list b -> list (pair a b)
help2 nil nil = nil
help2 (h::t) l2 = (help1 h l2)++(help2 t l2)

set_product (mkSet la) (mkSet lb) = (mkSet (help2 la lb))

--set_eql: (eq a) => (s1: set a) -> (s2: set a) -> bool
set_eql l1 nil = false
set_eql nil l2 = false
set_eql l1 l2 = set_existsp l1 l2

--set_toString: (Serialize a) => set a -> String
set_toString [1,2] = "One Two"
