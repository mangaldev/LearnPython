# Using list to Create a Python Stack
import collections

# stack = []
# stack.append("my")
# stack.append("name")
# stack.append("is")
# stack.append("Beacon")
#
# print("After append", stack)
# a = stack.pop()
# print("Pooped -> ", a)
# print("After pop ", stack)
#
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# if len(stack) > 0:
#     print(stack.pop())

# if len(stack) > 0:  # checking if stack is empty or not
#     print(stack.pop())  # Error here

# Using collections.deque to Create a Python Stack

stack = collections.deque()
stack.append('my')
stack.append('name')
stack.append('is')
stack.append('Beacon')

print("After append", stack)
a = stack.pop()
print("Pooped -> ", a)
print("After pop ", stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

if len(stack) > 0:  # checking if stack is empty or not
    print(stack.pop())  # Error here
