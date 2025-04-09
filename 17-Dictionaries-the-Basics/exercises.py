# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}

def to_dictionary(words: list[str]) -> dict:
    return {word: i for i, word in enumerate(words)}

print(to_dictionary(["value1", "value2"]))


# Define a length_counts function that accepts a list of strings.
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters,
# 2 strings with 7 letters, and 1 string with 4 letters.

sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]

def length_counts(words: list[str]):
    counts = {}
    for word in words:
        length = len(word)
        cur_val = counts.get(length, 0)
        counts[length] = cur_val + 1
    return counts


print(length_counts(sa_countries))



# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings.
# For each string in the list, if the string exists as a dictionary key,
# delete the key-value pair from the dictionary.
#
# If the string does not exist as a dictionary key, avoid an error.
# The return value should be the modified dictionary object.
#
# EXAMPLE:
# my_dict = {
#   "A": 1,
#   "B": 2,
#   "C": 3
# }
#
# strings = ["A", "C"]
# delete_keys(my_dict, strings) => {'B': 2}


strings = ["A", "C"]
my_dict = {
  "A": 1,
  "B": 2,
  "C": 3,
  "D": 4,
}

def delete_keys(dic, strs):
    for e in strs:
        dic.pop(e, None)
    return dic

print(delete_keys(my_dict, strings))