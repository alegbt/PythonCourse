## Immutable fixed length list that cannot be modified or changed after it is created
## can hold any type of elements (int str etc. together)

tupleSyntax1 = "a", "b", "c"
tupleSyntax2 = ("a", "b", "c")  ##funzionano entrambe le syntax ma la 2 e' la piu usata

emptyTupleSyntax = ()

oneElementSyntax = (1,)  ##senza la virgola sarebbe 1 con operatori di parentesi tonde

print(tupleSyntax1[0])  ##a
print(tupleSyntax1[-1])  ##c

tupleLists = (["asd", "sss"], ["aaa", "bbb"])
tupleLists[0][
    0] = "abc"  ##non posso modificare la struttura del tuple con tupleList[0] ma posso modificare la lista dentro il tuple

## Tuple function - converte 1 elemento in un tuple (qui converte 1 list)
print(tuple(["a", "b"]))

##TUPLE UNPACKING - destructuring di js

employee = ("bob", "john", "manager", 30)

##login syntax
# first_name = employee[0]
# last_name = employee[1]
# position = employee[2]
# age = employee[3]

#destructuring del tuple - combaciando le variables che usi con i valori del tuple le assegna automaticamente
first_name, last_name, position, age = employee
print(first_name, last_name, position, age)
## se ci fossero state un numero inesatto di values (3 o 5) avremmo avuto errore


##SWAP VALUES - con il principio di destructuring di prima possiamo cambiare le values inline

a = 1
b = 2
b, a = a, b
print(a, b)  #2 1

## MULTIPLE ASSIGN IN A TUPLE - con * su 1 elemento prima ke finsica il tuple si assegnano tutti gli
## elementi rimasti meno quante variabili ci sono dopo alla variabile con *

vals = ("asd", "bbb", "ccc", "ddd", 50)
first, *sec, third = vals
print(sec)  ##['ccc', 'ddd']
print(third)  ##50


## VARIABLE NUMBER OF ARGS IN A FUNCTION - stessa regola di prima, se c'e prima un *allargs e dopo 1 valore nei
## param della funzione va messo con ,argName = valore


def multi_args(*args):
    print(args)

multi_args(1, 2, 4)  #(1, 2, 4)


def maxN(*nums, notUseful):
    print(notUseful)
    return max(nums)

print(maxN(1, 2, 3, 4, 5, notUseful="not"))




##UNPACK ARGUMENTS TO FUNCTIONS

def product(a, b):
    return a*b

nums = (3,5)

print(product(*nums)) ##se combaciano li assegna in ordine



