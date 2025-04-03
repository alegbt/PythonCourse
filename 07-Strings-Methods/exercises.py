# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")        => 3
# vowel_count("helicopter")    => 4
# vowel_count("ssh")           => 0

def countVowels(word: str):
    word.upper()
    return word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")


def find_my_letter(word: str, char):
    return word.find(char)


print(find_my_letter("ciao", "o"))


# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespace on both sides of the
# argument.
# It should also replace every occurrence of the letter "g" with the
# letter "z"
# and every occurence of a space with an exclamation point (!).
#
# fancy_cleanup("       geronimo crikey  ")   => "zeronimo!crikey"
# fancy_cleanup("       nonsense  ")          => "nonsense"
# fancy_cleanup("grade")                      => "zrade"


def fancy_cleanup(word: str):
    return word.strip().replace("g", "z").replace(" ", "!")


print(fancy_cleanup("       geronimo crikey  "))
