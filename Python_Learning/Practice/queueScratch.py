from collections import deque

queue = deque([2,4,6,8,5])
queue.append(10)
print(queue)

queue.popleft()
print(queue)
