# default parameters


def add(a=0, b=0):
    return a + b


print(add(2, 2))  # 4
print(add(2))  # 2
print(add())  # 0

########################################################################################################################

# None object
a = None


def subtr(a, b):
    print(a - b)


resul = subtr(5, 3)
print(resul)  # None, la funzione non ha return quindi e' Null


########################################################################################################################

# Function annotations
# con i : gli dico che tipo di data type mi aspetto di ricevere, con -> str il return che mi aspetto
# MA non c'e alcuno stop al compile, funziona lo stesso la funzione

def word_multiplier(word: str, times: int) -> str:
    return word * times


print(word_multiplier(4, "asd"))
print(word_multiplier("asd", 4))
