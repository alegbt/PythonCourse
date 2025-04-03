# Define a convert_to_currency function that accepts a single parameter (an integer).
# The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
#
# EXAMPLES:
# convert_to_currency(15)    => "$15"
# convert_to_currency(8)     => "$8\


def convert_to_currency(n):
    return "$" + str(n)


print(convert_to_currency(10))


# Define a string_adder function that accepts two strings (a and b) as arguments.
# It should return a concatenated version of the arguments with a space in between.
# If the user does not pass in arguments, both arguments should default to an empty string.
#
# EXAMPLES
# string_adder("Hello", "World")      => "Hello World"
# string_adder("Emilio", "Estevez")   => "Emilio Estevez"
# string_adder()                      => " "
# string_adder("Tiger")               => "Tiger "


def string_adder(a="", b=""):
    return a + b

print(string_adder("asd","fff"))
print(string_adder())