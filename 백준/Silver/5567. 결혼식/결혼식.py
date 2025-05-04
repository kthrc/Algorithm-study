from collections import deque

# 입력
n_peers = int(input())
n_arr = int(input())

# 그래프 초기화
graph = [[] for _ in range(n_peers + 1)]
visited = [False] * (n_peers + 1)

# 관계 입력
for _ in range(n_arr):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS 탐색 (시작 노드: 1번, 거리: 0)
def bfs(start):
    queue = deque()
    queue.append((start, 0))  # (노드 번호, 깊이)
    visited[start] = True  # 1번 본인 방문 처리

    while queue:
        current, depth = queue.popleft()

        # 2촌까지만 탐색
        if depth >= 2:
            continue

        for friend in graph[current]:
            if not visited[friend]:
                visited[friend] = True
                queue.append((friend, depth + 1))

bfs(1)

# 1번 본인 제외하고 초대할 친구 수
print(sum(visited) - 1)
