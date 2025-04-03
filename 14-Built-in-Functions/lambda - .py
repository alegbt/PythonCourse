
##LAMBDA - funzioni anonime usate solo 1 volta
## utili x le built in xke cosi non devi creare 1 funzione ausiliare

metals = ["gold", "silver", "platinum", "palladium"]

## lambda scritto prima fa si che sia 1 lambda, metal e' 1 param, dopo i : sei dentro la funzione, metals e' la list su cui
## operare la funzione su ogni elemento
print(list(filter(lambda metal: len(metal) > 5, metals)))
print(list(filter(lambda el: len(el) > 5, metals)))
print(list(filter(lambda word: "p" in word, metals)))

print(list(map(lambda word: word.count("l"), metals)))
print(list(map(lambda val: val.replace("s", "$"), metals)))




## ALL - e' una concatenazione di && per gli elementi di 1 list, un solo falsy value e restituisce false
##Definition:
# returns True if all elements in the iterable are truthy (or if the iterable is empty). Otherwise, it returns False.
print(all([True])) ##true
print(all([True, True])) ##true
print(all([True, False])) ##false
print(all([1,2,3])) ##true
print(all([1,0])) ##false
print(all(["asd","aa"])) ##true
print(all(["aa",""])) ##false
print(all([])) ##true


##ANY - concatenazione di || basta 1 solo elemento che soddisfi e restituisce true
##Definition: any(iterable) returns True if at least one element in the iterable is truthy.
# Otherwise, it returns False.

print(any([])) ##false
print(any([True, False])) ##true
print(any([False, False])) ##false


##MAX - returns maximum value in the list
print(max([1,2,3,4]))
print(max(["d","z","a"])) ##z
print(max(["d","z","A"])) ##z

##MIN - returns minimum value inthe list
print(min([1,2,3,4]))
print(min(["d","z","a"])) ##a
print(min(["d","Z","a"])) ##Z

##SUM - sums a list of values
print(sum([1,2,3,4])) ##10
print(sum([-1,2.5,3.122,4])) ##8.622


##FORMAT - come rappresentare i numeri
number = 0.123456789
print(format(number, "+f")) #0.123456789 f sta per floating number, lo rappresenta come floating number ma usa il tpye string
print(type(format(number, "f"))) #string
print(format(number, ".2f")) #0.12
print(format(number, ".1f")) #0.1
print(format(number, ".3f")) #0.123

print(format(0.5, "%")) #50.00000% (indica il numero come percentuale)
print(format(0.5, ".2%")) #50.00%
print(format(1234567, ",")) #1,234,567 (mette il simbolo ogni 3 cifre)