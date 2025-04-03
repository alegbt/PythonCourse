def output_text():
    print("asd 1")
    print("asd 2")
    print("asd 3")


output_text()


########################################################################################################################

def sum2n(n1, n2):
    return n1 + n2


print(sum2n(2, 3))


########################################################################################################################

# posso assegnare manualmente i valori
def subtract(n1, n2):
    return n2 - n1


print(subtract(n2=10, n1=6))


########################################################################################################################

# da quando assegno manualmente i valori non posso piu assegnare senza dichiararli manualmente
def letters(a, b, c):
    print(a, b, c)


letters("BBB", c="AAA", b="CCC")  # BBB CCC AAA


########################################################################################################################

# returning functions


def add(a, b):
    return a + b


result = add(2, 3)
print(result) #5

