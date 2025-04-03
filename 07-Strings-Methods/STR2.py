
#startswith() controlla se l'inizio della str inizia con una serie di characters

salutation = "Mr. Kermit the Frog"

print(salutation.startswith("Mr")) # T
print(salutation.startswith("M")) # T
print(salutation.startswith("Mr.")) # T
print(salutation.startswith("mr")) # F
print(salutation.startswith("Mr. K")) # T

#endswith() controlla partendo dall'ultima lettera a ritroso
print(salutation.endswith("g")) # T
print(salutation.endswith("og")) # T
print(salutation.endswith("Frog")) # T
print(salutation.endswith("frog")) # F





#.count() conta quante volte una serie di char appare nella parola

word = "queueing"
print(word.count("e")) # 2
print(word.count("ue")) # 2
print(word.count("UE")) # 0
print(word.count("u") + word.count("e")) # 4


#string manipulation

wordC = "ale gob pino"
print(wordC.capitalize()) #Ale gob pino
print(wordC.upper()) #ALE GOB PINO
print("ALE GOB PINO".lower()) #ale gob pino
print(wordC.title()) #Ale Gob Pino
print("aaBBcC".swapcase()) # AAbbCc

print("PINUGO COTOGNO".lower().title()) # Pinugo Cotogno