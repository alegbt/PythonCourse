# def sum_of_lengths(text: list):
#     sumE = 0
#     for t in text:
#         sumE += len(t)
#     return sumE
#
# sum_of_lengths(["Hello", "Bob"])
# sum_of_lengths(["Nonsense"])
# sum_of_lengths(["Nonsense", "or", "confidence"])
#
#
# def sum_of_n(nums: list):
#     sumE = 1
#     for t in nums:
#         sumE *= t
#     return sumE
#
# print(sum_of_n([1,2,3]))
# print(sum_of_n([4,5,6,7]))
# print(sum_of_n([10]))

# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#
# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

# def smallest(nums:list):
#     v = nums[0]
#     for n in nums:
#         v = n if n < v else v
#         return v
#
# print(smallest([-3, -2, -1]))

# Define a concatenate function that accepts a list of strings.
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

# def concatenate(words:list):
#     contactenated = ""
#     for word in words:
#         contactenated += word if len(word) > 2 else ""
#     return contactenated
#
# print(concatenate(["abc","de","fgh"]))


# Define a super_sum function that accepts a list of strings.
# The function should sum the index positions of the first occurence of the letter “s” in each word.
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

# def super_sum(vals:list):
#     val = 0
#     for w in vals:
#         if w.find("s") > 0:
#             val+=w.find("s")
#     return val
#
# print(super_sum(["mustache", "greatest"]))
#
# print(super_sum(["mustache", "greatest", "almost"]))


# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#
# EXAMPLES
# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1

# def in_list(val:list, word):
#     for i, e in enumerate(val):
#         if word == e:
#             return i
#
# strings = ["enchanted", "sparks fly", "long live"]
# print(in_list(strings, "sparks fly")) ##1
