module team

data name = Andrew | Bill | Charles
data teammem = mkTeam name Nat Nat Nat

andr: teammem
andr = mkTeam Andrew 175 130 23

bill: teammem
bill = mkTeam Bill 180 165 41

char: teammem
char = mkTeam Charles 156 200 32
