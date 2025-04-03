## MAP - funziona dando 1 funzione come 1 argument e gli elementi su cui eseguire la funzione come secondo
## ritorna un map object su cui si puo iterare

numbers = [4, 8, 15, 16, 23, 42]

def cube(number):
    return number ** 3

print(list(map(cube, numbers)))

animals = ["cat", "bear", "zebra", "donkey", "cheetah"]

animalsMap = map(len, animals)

for a in animalsMap:
    print(a)

print(list(map(len, animals)))



## FILTER - la funzione che passi deve ritornare 1 boolean
## la invoca su ogni elemento della lista passata
## ritorna 1 filter Object


animals = ["elephant", "horse", "cat", "giraffe", "cheetah", "dog"]

##maniera classica
long_words = [animal for animal in animals if len(animal) > 5]
print(long_words)

def is_long_animal(animal):
    return len(animal) > 5

print(list(filter(is_long_animal, animals)))