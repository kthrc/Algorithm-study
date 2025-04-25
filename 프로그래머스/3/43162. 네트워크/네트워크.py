def DFS(i, n, computers):
    visited[i] = True  # i번 컴퓨터 방문 처리
    for j in range(n):
        if computers[i][j] == 1 and not visited[j]:  # 연결되어 있고 방문 안 했으면
            DFS(j, n, computers)  # DFS로 계속 탐색

def solution(n, computers):
    global answer
    answer = 0  # 네트워크 개수
    global visited
    visited = [False] * n  # 방문 여부 초기화
    for i in range(n):
        if not visited[i]:  # 방문 안 한 컴퓨터면
            DFS(i, n, computers)  # DFS 시작
            answer += 1  # 네트워크 하나 추가
    return answer
