# haiku no if + time

from random import choice
import time


first_line = ["ősz a nyárra", "tél az őszre", "év az évre", "nap a napra",
              "bú a bajra", "baj a búra", "bűn a szívbe", "szó a szájra",
              "bor a vérbe", "tűz a gallyra", "pénz a zsebbe", "láz a testre",
              "pap a faszra", "fagy az ágra", "hír a hírre"]

second_line = ["hegyek", "dombok", "sziklák", "felhők", "falak"]

third_line = ["a kövezetre", "a sugárútra", "a kerületre", "a kikötőre",
              "az erőműre", "a helyőrségre", "a lábfejedre", "az asztalodra",
              "a társatokra", "a turistákra", "az állatokra", "a kirakatra",
              "a munkagépre", "a dédmamára", "a képernyőre", "a búzaföldre",
              "a sípályára", "a gyártelepre", "a Balatonra", "a puszta tájra",
              "a temetőre"]

print("ÁRNYÉK\n")
time.sleep(4)
print(f'Mint {choice(first_line)},') 
time.sleep(4) 
print(f'{choice(second_line)}árnyéka kúszik') 
time.sleep(4) 
print(f'{choice(third_line)}.')
time.sleep(4)

