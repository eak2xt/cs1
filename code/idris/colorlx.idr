module colorlx

import bool
import pair

data colorlx = red | yellow | green | cyan | blue | magenta

complement: colorlx -> colorlx
complement red = cyan
complement yellow = blue
complement green = magenta
complement cyan = red
complement blue = yellow
complement magenta = green

additive: colorlx -> bool
additive red = true
additive green = true
additive blue = true
additive b = false

subtractive: colorlx -> bool
subtractive red = false
subtractive green = false
subtractive blue = false
subtractive b = true

complements: pair colorlx colorlx -> bool
complements (mkPair red cyan) = true
complements (mkPair cyan red) = true
complements (mkPair green magenta) = true
complements (mkPair magenta green) = true
complements (mkPair blue yellow) = true
complements (mkPair yellow blue) = true
complements b = false

mixink: pair colorlx colorlx -> colorlx
mixink (mkPair magenta cyan) = blue
mixink (mkPair cyan magenta) = blue
mixink (mkPair cyan yellow) = green
mixink (mkPair yellow cyan) = green
mixink (mkPair yellow magenta) = red
mixink (mkPair magenta yellow) = red
