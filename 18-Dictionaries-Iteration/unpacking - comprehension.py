
# DICTIONARY UNPACKING
# come con il destructuring di js si puo destructurare un dictionary se le sue key
# corrispondono ai param della funzione

def sum_nums(num1, num2):
    return num1 + num2

numDic = {
    "num1": 3,
    "num2": 2,
}

print(sum_nums(**numDic)) #5


# DICTIONARY COMPREHENSION
# creare dictionary da elementi iterabili

values = ["val1", "val22", "val3333"]

newDic = { x: len(x) for x in values }
print(newDic) # {'val1': 4, 'val22': 5, 'val3333: 7}

word = "aabbac"
letters = { letter: word.count(letter) for letter in word }
print(letters) # {'a': 3, 'b': 2, 'c': 1}

# USE CASE WITH CONDITIONAL LOGIC
conditionalNewDic = { x: len(x) for x in values if len(x) >= 5 }
print(conditionalNewDic) # {'val22': 5, 'val3333': 7}


## INVERSION
## flip around key - values

dic1 = {'a': 1, 'b': 2, 'c': 3}
invertedDic1 = {
    value: key
    for key, value in dic1.items()
}
print(invertedDic1) # {1: 'a', 2: 'b', 3: 'c'}

## inverte key : value se value >= 3
invertedDic2 = {
    value                       # -> diventerà la NUOVA KEY se la condizione è vera (value < 3)
    if value < 3 else           # -> condizione: se value è minore di 3
    key                         # -> altrimenti usa la KEY originale come nuova KEY
    :
    key                         # -> diventerà la NUOVA VALUE se la condizione è vera (value < 3)
    if value < 3 else           # -> condizione: se value è minore di 3
    value                       # -> altrimenti usa il VALUE originale come nuova VALUE
    for key, value in dic1.items()  # -> ciclo su tutti i pair (key, value) nel dizionario originale
}



print(invertedDic2) # {1: 'a', 2: 'b', 3: 'c'}




