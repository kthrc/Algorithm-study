n, m = map(int, input().split())  # 행 열 입력
board = [input() for _ in range(n)]  # 보드 입력

min_cnt = 64  # 최대 8*8 = 64

# 모든 8*8 구간 탐색
for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0  # W로 시작하는 경우
        cnt2 = 0  # B로 시작하는 경우
        for x in range(8):     # ← 이 부분이 누락됐던 부분!
            for y in range(8):
                curr = board[i + x][j + y]
                if (x + y) % 2 == 0:  # 짝수 위치
                    if curr != 'W':
                        cnt1 += 1
                    if curr != 'B':
                        cnt2 += 1
                else:  # 홀수 위치
                    if curr != 'B':
                        cnt1 += 1
                    if curr != 'W':
                        cnt2 += 1
        min_cnt = min(min_cnt, cnt1, cnt2)

print(min_cnt)
