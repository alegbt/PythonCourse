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


complexity = [
    {
        "key1": True,
        "key2": True,
     },
    {
        1.2:[
            "val1",
            "val2",
        ],
        1.3:[
            "val1",
            "val2",
        ],
        1.4:[
            "val1",
            "val2",
        ],

    },
    {
        "key3": False,
        "key4": False,
     },
    {
        1.2: [
            "val1",
            "val2",
        ],
        1.3: [
            "val1",
            "val2",
        ],
        1.4: [
            "val1",
            "val2",
        ],
    },
]


# Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the values of
# **kwargs is greater than 100. It should return False otherwise.
#
# EXAMPLES:
# plenty_of_arguments(20, 30)                          => False
# plenty_of_arguments(a = 50, b = 75)                  => True
# plenty_of_arguments(a = 50, b = 25, c = 50)          => True
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)  => False
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)  => True


def plenty_of_arguments(a, b, **kwargs):
    tot_sum = 0
    for e in kwargs.values():
        tot_sum += e
    return True if tot_sum + a + b > 100 else False


# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
# channels = {
#   2: "CBS",
#   4: "NBC",
#   5: "FOX",
#   7: "ABC"
# }
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
#
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}








# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys.
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer
#
# coasters = {
#   "Kingda Ka": 139,
#   "Top Thrill Dragster": 130,
#   "Superman: Escape From Krypton": 126
# }
#
# coaster_conversion(coasters) => {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}





