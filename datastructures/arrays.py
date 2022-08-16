a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print(c)  # [1, 2, 3, 4, 5, 6]

a[0] = 10
print(c)  # [1, 2, 3, 4, 5, 6]


a = [[1],[2],[3]]
b = [[3],[4],[5]]
c = a + b
print(c)  # [[1], [2], [3], [3], [4], [5]]

a[0][0] = 10
# Modifying a nested array also changed the concatenated list here ?? This means here concatenatio was not a deep copy
print(c)  # [[10], [2], [3], [3], [4], [5]]

# with `=` assignment operator we normally get only a shallow copy for sets/lists/dicts, and a reference to the Class objects
# use import copy
# copy.copy(any object) will make a shallow copy for class objects or nested list
# copy.deepcopy(any object) will make a deep copy for class objects