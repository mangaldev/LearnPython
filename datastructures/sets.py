
simple_set = {1, 2, 3, }
simple_set.add(4)
print(simple_set)
simple_set.add(4)
print(simple_set)


modified_set = simple_set | {4, 5}
print(modified_set)

# # # # # # # # # # # # # # #

set1 = {"Compiler", "Duck Typing", "OOP"}
print(type(set1))
# Exists condition
print("Compiler" in set1)
print("OOOP" in set1)

# print(set1[0]) Will give error, as we can not go to a index in a set

#  How to iterate over a set
for item in set1:
    print(item)

# For indexed element, convert this set into a list
list1= list(set1)
print(list1[0])

# # # # # # # # # # # # # # #

