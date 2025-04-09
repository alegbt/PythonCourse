## DICTIONARY
## unordered data structure for declaring relationship between objects
## a mutable data structure of key - pair

# Accessing values

dictionary1 = {
    "Key1": "Val1",
    "Key2": "Val2",
    "Key3": "Val3",
}

dictionaryWithTuples = {
    (1,2,3): True,
    (1,2,3): False, ##2 key uguali risultano nella 2 cche sovrascrive la 1
}

print(dictionary1["Key1"]) #Val1
print(dictionaryWithTuples[(1,2,3)]) ##False
print(dictionaryWithTuples.get(1, ["fallback value"])) # ['fallback value'] - con get() puoi mettere 1 fallback value


print((1,2,3) in dictionaryWithTuples) #T
print("Key1" not in dictionary1) #F

if "Key2" in dictionary1:
    print(dictionary1["Key2"]) #Val2



## MODIFICARE ELEMENTI

dictionaryWithList = {
    "list1": ["list1val1", "list1val2"],
    "list2": ["list2val1", "list2val2"],
}

dictionaryWithList["list3"] = ["list3val1", "list3val2"]
dictionaryWithList["list1"] = ["list1val111", "list1val222"]

print(dictionaryWithList) #{'list1': ['list1val111', 'list1val222'], 'list2': ['list2val1', 'list2val2'], 'list3': ['list3val1', 'list3val2']}


#USE CASES

values = ["word1", "word2", "word3", "word1", "word1", "word2"]

def count_words(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

print(count_words(values))







