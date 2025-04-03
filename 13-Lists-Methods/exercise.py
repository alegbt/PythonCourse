# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

def encrypt_message(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""

    for letter in message:
        encrypted_letter_index_position = (alphabet.index(letter) + 2) % 26
        encrypted += alphabet[encrypted_letter_index_position]

    return encrypted



## (alphabet.index(letter) + 2) % 26 funziona xke se il numero a sinistra del % e' minore di quello a dx
## ritorna il numero a sx:
# 5 % 11 = 5
# 11 % 5 = 1
# 7 % 8 = 7




# Define a word_lengths function that accepts a string.
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]

def word_lengths(phrase):
    words = phrase.split(" ")
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

word_lengths("abc defghi lm a")
word_lengths("Mary Poppins was a nanny")

# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""


def cleanup(words):
    res = []
    for word in words:
        if word.strip():
            res.append(word)
    return " ".join(res)


print(cleanup(["cat", " ", "er", "", "pillar"]))









