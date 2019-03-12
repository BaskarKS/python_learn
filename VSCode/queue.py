from collections import deque

# queue = deque([])
# queue.append(10)
# queue.append(20)
# queue.append(30)

# while len(queue) > 0:
#     print(queue.popleft())

# if not queue:
#     print("Length of Queue:", len(queue))
#     print("Queue is Empty")

queue = deque([])
queue.append(10)
queue.append(20)
queue.append(30)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)
print(list(queue))
print(len(queue))
queue.popleft()
if not queue:
    print("Length of Queue:", len(queue))
    print("Queue is Empty")
