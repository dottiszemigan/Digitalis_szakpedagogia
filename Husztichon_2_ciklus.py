from random import choice
#Kölcsey Ferenc: HUSZT
 
#Bús düledékeiden, Husztnak romvára megállék;
#	Csend vala, felleg alól szállt fel az éjjeli hold.
#Szél kele most, mint sír szele kél; s a csarnok elontott
#	Oszlopi közt lebegő rémalak inte felém.
#És mond: Honfi, mit ér epedő kebel e romok ormán?
#	Régi kor árnya felé visszamerengni mit ér?
#Messze jövendővel komolyan vess öszve jelenkort;
#	Hass, alkoss, gyarapíts: s a haza fényre derűl!

hexameter = ["Bús düledékeiden, Husztnak romvára megállék" , "Szél kele most, mint sír szele kél; s a csarnok elontott" , "És mond: Honfi, mit ér epedő kebel e romok ormán?" , "Messze jövendővel komolyan vess öszve jelenkort;"]
pentameter =["Csend vala, felleg alól szállt fel az éjjeli hold." , "Oszlopi közt lebegő rémalak inte felém." , "Régi kor árnya felé visszamerengni mit ér?" , "Hass, alkoss, gyarapíts: s a haza fényre derűl!"]

print('Husztichon\n')
for i in range(2):
  print(f'{choice(hexameter)},\n{choice(pentameter)}\n')
