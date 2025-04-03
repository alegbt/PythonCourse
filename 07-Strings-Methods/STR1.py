


# .find() cerca la prima occurrence della PRECISA str - cerca DOVE e' 1 elemento
string1 = "Google Home"

print(string1.find("H"))  # 7
print(string1.find("Ho"))  # 7
print(string1.find("o"))  # 1
print(string1.find("a"))  # -1
print(string1.find("op"))  # -1

# parte dal 3 e trova la 1 occurrence
print(string1.find("o", 3))  # 8


# in si usa x vedere SE C"E un elemento
print("Ho" in string1)  # true


#.index() funziona come .find ma CRASHA se non trova l'oggetto cercato

print(string1.index("G")) #0
print(string1.index("Ho")) #7
print(string1.index("H")) #7
# print(string1.index("f")) # ValueError: substring not found


#rfind - trova l'ULTIMA occurrence della str cercata

text = "pino tavolino tavolpino "

print(text.rfind("pino")) # 19
