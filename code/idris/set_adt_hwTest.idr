import set_adt_hw

e: bool
e = isEmpty (mkSet nil)

st1: set a
st1 = (mkSet nil)

st2: set a
st2 = (mkSet l1)

lz: nat
lz = set_cardinality (mkSet nil)

ld1: list a
ld1 = list_difference nil l1
