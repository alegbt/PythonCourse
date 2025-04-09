# Declare an invert function that accepts a dictionary object.
# The function should return a new dictionary where the keys and values from the original dictionary are inverted.
# Each key should now be a value, and each value should be a key.
# Assume both the keys and values of the dictionary are immutable.
#
# EXAMPLE:
# my_dict = {
#   "A": "B",
#   "C": "D",
#   "E": "F"
# }
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}

my_dict = {
  "A": "B",
  "C": "D",
  "E": "F"
}

def invert(dic):
    newDic = {}
    for key, value in dic.items():
        newDic.setdefault(value, key)
    return newDic

print(invert(my_dict))


# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears
# as a value among the dictionary’s values.
#
# EXAMPLE:
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1

my_dict = { "a" : 5, "b" : 3, "c" : 5 }

def count_of_value(dic, num):
    res = 0
    for key, value in dic.items():
        if value == num:
            res+=1
    return res

print(count_of_value(my_dict, 3))




# Declare a sum_of_values function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
# my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])            => 5
# sum_of_values(my_dict, ["a", "c"])       => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])            => 0

my_dict = { "a": 5, "b": 3, "c": 10 }

def sum_of_values(dic: dict, vals: list) -> int:
    num_sum = 0
    for e in vals:
        num_sum += dic[e]
    return num_sum

def sum_of_values2(dic: dict, vals: list) -> int:
    num_sum = 0
    for key, value in dic.items():
        if key in vals:
            num_sum += value
    return num_sum

print(sum_of_values2(my_dict, ["a", "c"]))





# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]

my_dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}

def common_elements(dic):
    res = []
    for e in dic:
        if e in dic.values():
            res.append(e)
    return res


def common_elements2(dic):
    return [key for key in dic.keys() if key in dic.values()]




print(common_elements2(my_dict))







# Assign a list of four dictionaries to a "complexity" variable below

# The first and third dictionaries should have two key-value pairs
# For those dictionaries, the keys should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For those dictionaries, the keys shoulds be floats and the values should be list of strings.
# The lists can be of any length.







