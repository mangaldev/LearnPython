coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v = zip(*result_list)
print('c =', c)
print('v =', v)

list = [(1, 2, 3), (4, 5)]
a, b = zip(*list)
print("a = ", a)
print("b = ", b)
