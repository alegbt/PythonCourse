

# elif e' ugugale a else if
def positive_or_negative(number):
    if number > 0:
        print("positive")
    elif number < 0:
        print("num is negative")
    else:
        print("num is 0")

positive_or_negative(3) #positive
positive_or_negative(-3) #negative
positive_or_negative(0) # num is 0


# conditional expression - funziona solo con 2 outcome (ternary operator)
zip_code = "90210"
#maniera lunga
if len(zip_code) == 5:
    check = "Valid"
else:
    check = "Invalid"

#maniera corta
check = "Valid" if len(zip_code) == 5 else "Invalid"
print(check) #Valid



# AND keyword

if 5 < 7 and "rain" == "rain":
    print("both condition are true")

if 5 < 7 and "asd" == "rain":
    print("at least 1 condition is not true")

value = 91
if 90 < value < 100:
    print(f"{value} is in between 90 and 100 ")


# OR keyword

if 5 > 8 or 7 < 11:
    print("at least 1 is true")


# NOT keyword

print(not True) # False
print(not False) # True

if "h" not in "Hello":
    print("h is not in Hello")

value = 10
if not value > 100:
    print("this will print")

