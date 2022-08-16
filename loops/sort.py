data = [10, 9, 1, 100]
# natural order is ascending order
print(sorted(data))
print(sorted(data, reverse=True))

data = (10, 9, 1, 100)
# Note that result will be a list again
print(sorted(data))  # [1, 9, 10, 100]

data = [{"a": 100, "b": 4}, {"f": 200, "b": 3}]
sorted_data = sorted(data, key=lambda x: x["b"])
print(sorted_data)

# Sorting a dictionary
dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)
sorted_keys_list = sorted(dict.keys())
sorted_dict = {}
for i, item in enumerate(sorted_keys_list):
    sorted_dict[item] = dict[item]
print(sorted_dict)
