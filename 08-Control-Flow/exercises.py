# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2)    => "even"
# even_or_odd(0)    => "even"
# even_or_odd(13)   => "odd"
# even_or_odd(9)    => "odd"
def even_or_odd(num: int):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


even_or_odd(3)


def truthy_or_falsy(arg):
    if bool(arg):
        print("truthy")
    else:
        print("falsy")


truthy_or_falsy(0)
truthy_or_falsy("asd")


# Declare a negative_energy function that accepts a numeric argument and returns its absolute value.
# The absolute value is the number's distance from zero.
#
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0


def negative_energy(num: int):
    if num < 0:
        return num * -1
    else:
        return num


print(negative_energy(5))
print(negative_energy(-5))
print(negative_energy(0))


# Define a divisible_by_three_and_four function that accepts a number as its argument.
# It should return True if the number is evenly divisible by both 3 and 4 .
# It should return False otherwise.
#
# divisible_by_three_and_four(3)   => False
# divisible_by_three_and_four(4)   => False
# divisible_by_three_and_four(12)  => True
# divisible_by_three_and_four(18)  => False
# divisible_by_three_and_four(24)  => True


def divby3and4(num: int):
    v = True if num % 3 == 0 and num % 4 == 0 else False
    return v


# print(divby3and4(12))
# print(divby3and4(13))


# FizzBuzz is a popular programming problem to test a developer's ability to think logically with code.
# The problem is simple but deceptive.
# Define a fizzbuzz function that accepts a single number as an argument. The function should print every number from 1 to that argument.
# There are a couple caveats.
# If the number is divisible by 3, print "Fizz" instead of the number.
# If the number is divisible by 5, print "Buzz" instead of the number.
# If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.
# If the number is not divisible by either 3 or 5, just print the number.


def fizzBuzz(num: int):
    n = 0
    while n < num:
        n += 1
        if n % 3 == 0 and n % 5 == 0:
            print(f"{n} is FizzBuzz")
        elif n % 3 == 0:
            print(f"{n} is Fizz")
        elif n % 5 == 0:
            print(f"{n} is Buzz")
        else:
            print(f"{n} is neither")


#fizzBuzz(1)


# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number.
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120
#
# Return the factorial calculation from your function. You should NOT use any kind of loops.
# Instead, utilize recursion. Your function MUST call itself.
# See sample inputs and return values below
#
# factorial(1) => 1
# factorial(2) => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120


def factorial(num: int):
    if num == 1:
        return num * 1
    return num*factorial(num-1)


print(factorial(6))
