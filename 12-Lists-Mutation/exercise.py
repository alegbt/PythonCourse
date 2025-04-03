# Given the great_directors list below, overwrite the “Steven Spielberg” string with a string of “Michael Bay”.
from functools import total_ordering

great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]


# Given the transformers list below, overwrite “Bumblebee” with “Grimlock”.
transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]


# Given the camping_trip_supplies list below, overwrite "Socks" with "Food".
camping_trip_supplies = ["Socks", "Flashlight", "Tent", "Blanket"]


# Given the tech_companies list below, overwrite the Microsoft, Blackberry, and IBM strings
# with the strings “Facebook” and “Apple”. Use list slicing syntax.
tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]


great_directors[1:2] = ("a")
# print(great_directors)

tech_companies[1:4] = ["a","b"]
# print(tech_companies)





# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# EXAMPLES
# sum_from(1, 2)   # 1 + 2                  => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42

def sum_from(less, more):
    total = 0
    for number in range(less, more + 1):
        total += number
    return total



# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions
# in which the two lists have equal elements
#
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])  => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])  => [1, 3]


def same_index_values(list1, list2):
    result = []
    for i, val in enumerate(list1):
        if list2[i] == val:
            result.append(i)
    return result
