# Define a long_word function that accepts a string.
# The function should return a Boolean that reflects whether the string has more than 7 characters.
#
# EXAMPLES:
# long_word("Python")         => False
# long_word("magnificent")    => True


def long_word(word: str):
    return len(word) > 7


print(long_word("aaaaaaaa"))
print(long_word("aaaaaaa"))


# Define a same_first_and_last_letter function that accepts a string as an argument.
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner")   => True
# same_first_and_last_letter("Runner")   => False
# same_first_and_last_letter("clock")    => False
# same_first_and_last_letter("q")        => True


def same_first_and_last_letter(word: str):
    return word[0] == word[-1]


print(same_first_and_last_letter("abca"))
print(same_first_and_last_letter("abcaf"))





# Define a first_three_characters function that accepts a string argument.
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty")   => "dyn"
# first_three_characters("empire")    => "emp"


def first_three_characters(word):
    return word[:3:]

print(first_three_characters("cijljlao"))
