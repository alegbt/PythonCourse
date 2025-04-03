# List
# Store objects in order
# You can mix data types in a list

# modi x dichiarare 1 list
empty_list = []
empty2 = list()

sodas = ["Coke", "Fanta", "Pepsi"]
print(len(sodas))  # 3

###################################################################################

# Controlla se 1 list ha 1 certa value - la str deve essere esatta

meals = ["breakfast", "lunch", "dinner"]

print("lunch" in meals)  # True
print("lun" in meals)  # False

scores = [99.0, 1, 23]

print(99 in scores)  # T
print(2 in scores)  # F
print(2 not in scores)  # T

###################################################################################


numberi = ["ciao", 2, 3, 4, 5, 6, 7]

print(numberi[1]) # 2
print(numberi[5]) # 6

#se l'elemento e' indexable allora la seconda quadra prende il valore a quell'index

print(numberi[0][3]) # o
print(numberi[-7][1]) # i



