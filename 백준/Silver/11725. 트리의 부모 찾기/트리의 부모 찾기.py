import sys
sys.setrecursionlimit(10**6)  # 깊이 제한 확장 (많은 노드 대비)

# 여기서 부모 설정
def DFS(node):
    # 현재 노드 -> 방문 처리
    visited[node] = True
    # 반복문 돌리면서 그래프 탐색
    for now in graph[node]:
        if not visited[now]:
            # 아직 방문하지 않은 노드는 현재 노드가 부모
            findParent[now] = node
            # 자식 노드에 대해 DFS 재귀 호출
            DFS(now)

# 노드 개수 입력 받기
n_node = int(input())

# DFS 처리를 위한 변수
graph = [[] for _ in range(n_node + 1)]
visited = [False] * (n_node + 1)
findParent = [0] * (n_node + 1)

# (n_node - 1)개 만큼 관계 개수를 받음
for i in range(n_node - 1):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

# DFS 실행
DFS(1)

# 부모 출력(루트노드(1) 제외한 2~맨 끝까지)
for j in range(2, n_node + 1):
    print(findParent[j]) 