def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

n_computer = int(input())
n_link = int(input())

# 빈 그래프 생성
graph = [[] for _ in range(n_computer+1)]
stack = []

# 1번 컴퓨터부터 시작
visited = [False] * (n_computer + 1)
for i in range(n_link):
    a, b = map(int, input().split(' '))
        
    # 양방향
    graph[a].append(b)
    graph[b].append(a)

# 1번 컴퓨터부터 시작
dfs(1)   

# 방문횟수 합산(1번 컴퓨터 제외)
print(sum(visited)-1)
