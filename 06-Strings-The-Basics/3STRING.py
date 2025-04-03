


#IN operator, controlla se qualcosa e' in qualcosa

phrase = "The winners of the prize are Boris, Andy, and Adam"

print("Boris" in phrase) #true
print("Bor" in phrase) #true
print("boris" in phrase) #false
print(" " in phrase) #true

bol = "a" in phrase
print(bol) #true

#NOT IN controlla se qualcosa NON e' in qualcosa

print("Boris" not in phrase) #true
print("boris" not in phrase)
