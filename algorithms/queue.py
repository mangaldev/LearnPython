import collections



queue = []
queue.append("my")
queue.append("name")
queue.append("is")
queue.append("Beacon")

print("After append", queue)
a = queue.pop()
print("Pooped -> ", a)
print("After pop ", queue)

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

queue = collections.deque()
queue.append('my')
queue.append('name')
queue.append('is')
queue.append('Beacon')

print("After append", queue)
a = queue.pop()
print("Pooped -> ", a)
print("After pop ", queue)

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
