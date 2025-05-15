
# **kwargs permette di definire un gruppo di variabili durante l'invocamento  della funzione
# viene resituito un dictionary con: nome variabile : value
# si puo usare insieme a parametri singoli e gruppi di *args

def length(word):
    return len(word)

print(length("Hello")) #5
print(length(word = "Hello")) #5

# print(length(something = "Hello")) #error
# print(length(word = "Hello", something = "Goodbye")) #error

#kwarg permette di dichiarare i valori i nvariabili contentute nei param della funzione invocata
def collect_keyword_arguments(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"The key is {key} and the value is {value}")

#{'a': 2, 'b': 3}
#<class 'dict'>
#The key is a and the value is 2
#The key is b and the value is 3
collect_keyword_arguments(a = 2, b = 3)



# Con a, b , *args, **kwargs :
# prende il 1 e 2 elemento come a e b, tutti i successivi in *arg
# e tutti quelli indicati con variabili in **kwargs
def args_and_kwargs(a, b, *args, **kwargs):
    print(f"The total of your regular arguments a and b is {a + b}")
    print(f"The total of your args tuple is {sum(args)}")

    dict_total = 0
    for value in kwargs.values():
        dict_total += value
    print(f"total of kwarg is {dict_total}")

#The total of your regular arguments a and b is 3
# The total of your args tuple is 18
# total of kwarg is 23
args_and_kwargs(1, 2, 3, 4, 5, 6, x=8, y=10, z =5)