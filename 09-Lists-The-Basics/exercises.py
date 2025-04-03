# Define a first_and_last function that accepts a list of strings.
# The function should return a concatenation of the first element and the last element.
# Assume the list will always have 1 or more elements.
#
# first_and_last(["a", "b", "c"])        => "ac"
# first_and_last(["bob", "tom", "rob"])  => "bobrob"
# first_and_last(["a"])                  => "aa"


def first_and_last(strs: list):
    return strs[0] + " " + strs[len(strs) - 1]


print(first_and_last(["ciao", "pino", "ugo"]))



# Declare a nested_extraction function that accepts a list of lists and an index position.
#
# The function should use the index as the basis of finding both the nested list
# and the element from that list with the given index position
#
# You can assume the number of lists will always be equal to
# the number of elements within each of them.
#
# nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
# nested_extraction(nl, 0)  => 3
# nested_extraction(nl, 1)  => 8
# nested_extraction(nl, 2)  => 12


def nested_extraction(nestL:[[]], i:int):
    print(nestL[i][i])


nested_extraction([[3, 4, 5], [7, 8, 9], [10, 11, 12]], 2)
