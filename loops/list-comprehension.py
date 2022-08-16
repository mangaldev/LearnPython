# list = [1, 2, 3, 4]
# squares = []
# for item in list:
#     squares.append(item * item)
#
# def some_operation(i, j):
#     return str(str(i) + " " + str(j))
#
# list = [ some_operation(i,item) for i, item in enumerate(list)]
# print(list)

dictionary = {"key1": "value1", "key2": "value2"}
modified_dict = { item[0]+"_new": item[1]+"_new" for item in dictionary.items() }
print(modified_dict) # {'key1_new': 'value1_new', 'key2_new': 'value2_new'}