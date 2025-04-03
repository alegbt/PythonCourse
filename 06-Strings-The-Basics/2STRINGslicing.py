
address = "Via pino ugo, pinughia, San Pino"

# 0 incluso 5 escluso
print(address[0:5])  # Via p

# da -8 a -5 le prende - parte da 8 character dalla fine e si ferma a -5
print(address[-8:-5])  # San

# da 4 in poi
print(address[4:])  # pino ugo, pinughia, San Pino



alphabet = "abcdefghijklmnopqrstuvwxyz"

# printa da 0 a 10 ogni 2 string letter
print(alphabet[0:10:2])  # acegi

# printa da 0 a 26 orni 5 caratteri
print(alphabet[0:26:5])  # afkpuz

# se tolgo il 1 prende il valore di default, nel caso del primo valore parte dall'inizio
print(alphabet[:26:5])  # afkpuz

# parte dall'inizio, finisce alla fine e prende ogni 5 (inizio e fine sono messi di default con :: )
print(alphabet[::5])  # afkpuz

# parte da -20 fino a -8 e prende ogni 5
print(alphabet[-20:-8:5])  # glq

# parte dall'ultimo e va indietro e prende ogni 5
print(alphabet[::-5])




##################################################################################################################

# print special character

print(" \"To be or not to be\" hamlet  ")
print(' \'To be or not to be\' hamlet  ')
print(' print 3 \\\\\\  ')

# RAW strings - mettendo r davanti 1 str diventa raw, non vede simboli o cose speciali

file_path_raw = r"C:\ale\documents"

print(file_path_raw)


#how to break arguments on multiple lines
numberWIthLongNameThatShouldBeShorter = 5
n2 = 12
veryLongLineUsedAsAVariableNameThatShouldntBeThatLong = 13

sum1 = numberWIthLongNameThatShouldBeShorter + \
      n2 + \
      veryLongLineUsedAsAVariableNameThatShouldntBeThatLong

print(sum1)


