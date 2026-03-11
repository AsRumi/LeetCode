from collections import deque

q = deque()
q.append(['R', 'available'])
q.append(['R', 'available'])
q.append(['R', 'available'])
q.append(['R', 'available'])
q.append(['R', 'available'])
counter = 0
while counter < 3:
    q[counter] = ["R", 'unavailable']
    counter += 1
print(q)