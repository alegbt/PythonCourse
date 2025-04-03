# .islower .isupper , controlla che sia TUTTO in upper o lower case

print("asdsa 123sa$".islower()) # T
print("asdsa 123Da$".islower()) # F
print("ASDP1!2".isupper()) # T
print("AAAsdw12!".isupper()) # F


# isTitle true se usa il title case x ogni parola altrimenti F

print("Ciao Pino Ugo".istitle()) # T
print("Ciao 2 Ugo".istitle()) # T
print("Ciao Pino ugo".istitle()) # F


# isalpha e isnumeric - controlla se sono tutti parte dell'alfabeto o numeri
print("csias".isalpha()) # T
print("csias1".isalpha()) # F
print("1231".isnumeric()) # T
print("1231!".isnumeric()) # F
print("csias1".isnumeric()) # F


# isalnum - controlla se tutto e' alfanumerico (non compreso di spazi o simboli)
print("ciao123".isalnum()) # T
print("ciao 123".isalnum()) # F

# isspace - controlla se sono SOLO spazi

print("   ".isspace()) # T
print(" d  ".isspace()) # F
print("  2 ".isspace()) # F


