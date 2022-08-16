a_list = ['learnig', 'python', 'at', 'beacon', 'fire']

for i in range(len(a_list) - 1, -1, -1):
    print(a_list[i])
#  Plain print of items
# for item in a_list:
#     print(item)

# #  Now need indexing of items
# for index in range(len(a_list)):
#     print(index, a_list[index])
#
# for item in enumerate(a_list):
#     print(item)
#     print(item[0], item[1])
#
# for (index, item) in enumerate(a_list):
#     print(index, item)
#
#
dictionary = {"key1": "value1", "key2": "value2"}
# for key in dictionary:
#     print(key, dictionary[key])
#
for item in dictionary.items():
    print(item)
