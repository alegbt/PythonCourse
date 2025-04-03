
#a = input("x - y  Type x: ")
#b = input(f"{a} - y  Type y: ")
a = 10
b = 4

if int(a) > int(b):
    print(f"{a} - {b} = {int(a) - int(b)}")

# TRUTHINESS AND FALSYNESS
if 10 > 3:
    print("hello")
if 3:
    print("hello2")
if "asd":
    print("hello3")
if 0:
    print("wont print")

# bool() restituisce se e' true o false l'elemento dentro
print(bool(1)) # true
print(bool("asd")) # true
print(bool("0")) # true
print(bool(0)) # false
