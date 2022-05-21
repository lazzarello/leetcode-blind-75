# https://realpython.com/linked-lists-python/
from collections import deque
from time import sleep

queue = deque()

for person in ["Mary", "John", "Susan"]:
    queue.append(person)

print(queue)
print('Added these three to the queue')
sleep(5)

for _ in range(3):
    print(queue.popleft())

print(queue)
print('empty the queue')
