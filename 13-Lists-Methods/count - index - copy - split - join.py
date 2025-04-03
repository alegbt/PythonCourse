##COUNT - restiotuisce numero di quante volte 1 elemento e' presente

vals = ["asd", "bde", "wer", "asd"]
print(vals.count("asd")) #2

##INDEX - restituisce la index del valore per cui searcha, si riferisce solo alla prima occorrenza

print(vals.index("bde")) ##1
print(vals.index("asd")) ##0

if "aaa" in vals:
    print(vals.index("aaa"))

print(vals.index("asd", 1)) ##3


## COPY - create shallow copy of objects
copied = vals.copy()


## SPLIT - split a string based on a recurring occurrence
## returns a list
## first argument = the divider, second argument = how many times to split

users = "bob, Dave, Ugo, Pino"
print(users.split(", ")) ##['bob', 'Dave', 'Ugo', 'Pino']
print(users.split(", ", 1)) ##['bob', 'Dave, Ugo, Pino'] ##ha splittato solo la 1 occorrenza


## JOIN - joina + strings in 1 lista con 1 custom separator indicato

address = ["via pino", "roma", "RM"]
print(", ".join(address)) ##via pino, roma, RM
print("-".join(["334","123","8574"])) ##334-123-8574