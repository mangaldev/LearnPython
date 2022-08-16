# finbonacci sequence => 1 1 2 3 5 8 13 21 34 55 89  .....

dict[1] = 1
dict[0] = 1
def fib(i: int, dict):
    if (dict[i]):
        return dict[i]
    dict[i] = fib(i - 1) + fib(i - 2)
    return dict[i]

# complexity ==> O(N)

print(fib(10))
# print(fib(4))


# # Time Complexity ?
#
# # Factorial => 5 * 4  * 3 * 2 * 1
# def fact(i: int):
#     if i <= 1:
#         return 1
#     return i * fact(i - 1)
#
#
# print(fact(5))
