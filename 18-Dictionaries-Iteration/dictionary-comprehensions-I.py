
#FOR

dictionary1 = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}


for key in dictionary1:
    print(f"The key is {key} and the value is {dictionary1[key]}")


# ITEMS method
# returns a list of the key - value
# first element in the for is a key and the second is a value

dictionary2 = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

for key, value in dictionary2.items():
    print(f"The key is {key} and the value is {value}")


## KEYS and VALUES  methods

dictionary3 = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}


print(dictionary3.keys()) #dict_keys(['key1', 'key2', 'key3'])
print(dictionary3.values()) #dict_values(['value1', 'value2', 'value3'])


for el in dictionary1.keys():
    print(f"Keys are are {el}")

# Keys are key1
# Keys are key2
# Keys are key3

for el in dictionary1.values():
    print(f"Values are {el}")

# Values are value1
# Values are value2
# Values are value3

##Use cases

print("key1" in dictionary3.keys()) #TRUE
print("value4" in dictionary3.values()) #FALSE



## SORTED function
## sort by key order

nums = [2,3,1,5]
print(sorted(nums)) #[1, 2, 3, 5]

dic1 = {
    "key2":"value2",
    "key1":"value3",
    "key3":"value1"
}

print(sorted(dic1)) #['key1', 'key2', 'key3']


for key, value in sorted(dic1.items()):
    print(f"key is {key} value is {value}")

# key is key1 value is value3
# key is key2 value is value2
# key is key3 value is value1



## LIST OF DICTIONARIES

list_of_dict = [
    {
        "key1section1":"value1",
        "key2section1":"value2",
        "key3section1":"value3",
     },
    {
        "key1section2":"value1",
        "key2section2":"value2",
        "key3section2":"value3",
    }
]


for i, el in enumerate(list_of_dict):
    for key, value in el.items():
        print(f" dictionary {i} key = {key} value = {value}")