
##ZIP - combina diverse liste e puoi lavorare con i vari valori alla stessa index alla volta

list1 = [1,2,3,4,5]
list2 = [11,22,33,44,55]
list3 = [111,222,333,444,555]

for l1, l2, l3 in zip(list1, list2, list3):
    print(l1, l2, l3) ##1 11 111 - 2 22 222 - 3 33 333 ...


##LIST COMPREHENSION - syntax:
## [OPERATION for ELEMENT in LIST] returns List operated on
## OPERATION e' anche quello che vuoi che sia aggiunto nella nuova lista, quindi se c'e un if dopo puo essere
## [donut for donut in donuts if "Cream" in donut]
## permette di non lasciare variabili in memoria come si fa con " for n in numbers " dove n resta poi in memoria
## anche dopo ed e' piu conciso
numbers = [2,3,4,5]
squares = [n ** 2 for n in numbers]
print(squares)

words = ["asd", "aaaa"]
print([len(word) for word in words])

##ADVANCED USES

##itera ogni char di "donut" e mette la index nella list che poi ritorna
print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"]) ##[3, 14, 13, 20, 19]

##itera numeri da 0 a 19 e divide per 2
print([number / 2 for number in range(20)]) ##[0.0, 0.5, 1.0, 1.5, 2.0, 2.5..]

donuts = [
    "Boston Cream",
    "Jelly",
    "Vanilla Cream",
    "Glazed",
    "Chocolate Cream"
]

# creamy_donuts = []
# for donut in donuts:
#     if "Cream" in donut:
#         creamy_donuts.append(donut)

##se l'elemento "donut" del ciclo rispetta l'if viene aggiunto alla List
creamy_donuts = [donut for donut in donuts if "Cream" in donut]
print(creamy_donuts)

print([len(donut) for donut in donuts if "Cream" in donut])

print([donut.split(" ")[0] for donut in donuts if "Cream" in donut])
