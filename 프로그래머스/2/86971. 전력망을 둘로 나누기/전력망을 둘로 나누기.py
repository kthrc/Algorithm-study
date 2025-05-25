def dfs(current, graph, visited):
    visited[current] = True
    count = 1  # 현재 노드도 포함

    for next_node in graph[current]:
        if not visited[next_node]:
            count += dfs(next_node, graph, visited)  # 연결된 노드 계속 탐색

    return count  # 연결된 노드 수 반환

def solution(n, wires):
    min_diff = n  # 차이의 최댓값으로 초기화

    for i in range(len(wires)):
        # 끊을 간선을 제외하고 그래프 만들기
        graph = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n + 1)  # 방문 배열
        group_size = dfs(1, graph, visited)  # 한쪽 그룹의 노드 수
        diff = abs(n - group_size - group_size)  # 두 그룹 차이
        min_diff = min(min_diff, diff)  # 최소값 갱신

    return min_diff
