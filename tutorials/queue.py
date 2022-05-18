from collections import deque
from time import sleep
queue = deque()
queue


queue.append("Mary")
queue.append("John")
queue.append("Susan")
print(queue)
print('Added these three to the queue')
sleep(10)
for _ in range(3):
    print(queue.popleft())
print(queue)
print('empty the queue')
