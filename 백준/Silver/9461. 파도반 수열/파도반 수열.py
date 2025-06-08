t = int(input())  # 테케 수 입력

# 파도반 저장 배열
pado = [0] * 101
pado[1], pado[2], pado[3] = 1, 1, 1
pado[4], pado[5] = 2, 2

# 배열 초기값을 제외한 점화식
for i in range(6, 101):
    pado[i] = pado[i - 1] + pado[i - 5]

# 각 테스트 케이스 결과 출력
for _ in range(t):
    n = int(input())
    print(pado[n])
