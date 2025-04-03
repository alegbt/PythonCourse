##INSERT
## .insert(index, object)
list1 = ["el1", "el2"]
list1.insert(1, "asd")
list1.insert(0, "eee")
print(list1) ##['eee', 'el1', 'asd', 'el2']


#POP - removes an element from a list and returns the element and modifies the list
removeEl = list1.pop()
print(removeEl) ##el2
print(list1) ##['eee', 'el1', 'asd']
removeEl2 = list1.pop(0)
print(removeEl2) ##eee
print(list1) ##['el1', 'asd']


#DEL - removes n elements from the list
list2 = ["el1", "el2", "el3", "el4", "el5"]
del list2[1]
print(list2) ##['el1', 'el3', 'el4', 'el5']
del list2[0:2]
print(list2) ##['el4', 'el5']

#REMOVE - removes specific value and modifies the list
##removes only the first occurence

list3 = ["asd", "qqq", "asd", "www"]
list3.remove("asd")
print(list3) ##['qqq', 'asd', 'www']

##CLEAR - removes all the elements in a list
list3.clear()
print(list3) ##[]


##REVERSE
list2.reverse()
print(list2) ##['el5', 'el4']

##SORT - modifica la list
## se numerica ascending order
## se string, le Capital letter vengono sortate prima delle minuscole

nums = [1,4,3,4,6,2]
nums.sort()
print(nums) ##[1, 2, 3, 4, 4, 6]
words = ["Abc", "Zcc", "Bzz", "abc"]
words.sort()
print(words) ##['Abc', 'Bzz', 'Zcc', 'abc']

##SORTED - ritorna sorted list non modificandola
nums2 = [1,2,5,4,4,3]
print(sorted(nums2)) ##[1, 2, 3, 4, 4, 5]
print(nums2) ##[1, 2, 5, 4, 4, 3]