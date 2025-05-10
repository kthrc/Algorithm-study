from collections import deque

n_people = int(input()) 
parent, child = map(int, input().split()) 
n_relation = int(input())

graph = [[] for _ in range(n_people + 1)]

for _ in range(n_relation):
    from_person, to_person = map(int, input().split())
    graph[from_person].append(to_person)
    graph[to_person].append(from_person)

visited = [False] * (n_people + 1)
level = [0] * (n_people + 1)

q = deque()
q.append(parent)
visited[parent] = True

while q:
    current_person = q.popleft()

    if current_person == child:
        break

    for neighbor in graph[current_person]:
        if not visited[neighbor]:
            visited[neighbor] = True
            level[neighbor] = level[current_person] + 1
            q.append(neighbor)

if visited[child]:
    print(level[child])
else:
    print(-1)
