def dfs(x):
    visited[x] = True
    next_node = graph[x]
    if not visited[next_node]:
        dfs(next_node)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    graph = [0] + arr  # 인덱스 1부터 사용
    visited = [False] * (n + 1)
    cycle_count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            cycle_count += 1

    print(cycle_count)