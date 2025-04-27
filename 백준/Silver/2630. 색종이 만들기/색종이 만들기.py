# 종이 크기 입력 받기
n = int(input())
paper = []

# 입력 받은 부분 2차원 리스트로 변환
for _ in range(n):
    row = list(map(int, input().split()))
    paper.append(row)

# 하얀색, 파란색 색종이 개수
white = 0
blue = 0

# 색종이 검사
def cut(x, y, size):
    # 전역변수로 선언
    global white
    global blue

    # 첫 번째 칸의 색
    color = paper[x][y]

    # 반으로 쪼개가면서 같은 색인지 검사
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                # 색이 다르면 4등분
                half = size // 2
                cut(x, y, half)  # 왼쪽 위
                cut(x, y + half, half)  # 오른쪽 위
                cut(x + half, y, half)  # 왼쪽 아래
                cut(x + half, y + half, half)  # 오른쪽 아래
                return  # 더 볼 필요 없음

    # 반복문이 끝날 때까지 같은색이면
    if color == 0:
        white = white + 1
    else:
        blue = blue + 1

# 처음에는 전체 종이를 검사
cut(0, 0, n)

# 출력
print(white)
print(blue)
