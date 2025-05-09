def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

n_computer = int(input())
n_link = int(input())

# 빈 그래프 생성
graph = [[] for _ in range(n_computer+1)]

# 1번 컴퓨터부터 시작
visited = [False] * (n_computer + 1)
for i in range(n_link):
    p1, p2 = map(int, input().split(' '))
        
    # 양방향
    graph[p1].append(p2)
    graph[p2].append(p1)

# 1번 컴퓨터부터 시작
dfs(1)   

# 방문횟수 합산(1번 컴퓨터 제외)
print(sum(visited)-1)
