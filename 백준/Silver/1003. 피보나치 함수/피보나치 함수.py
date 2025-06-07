# 0과 1이 몇 번 출력되는지 저장할 리스트 만들기
memo = [[-1, -1] for _ in range(41)]  # 최대 40(문제)

def fibonacci(n):
    # 이미 계산된 값이면 그대로 리턴
    if memo[n][0] != -1:
        return memo[n]

    # 기본값 설정
    if n == 0:
        memo[n] = [1, 0]  # 0이 1번, 1은 0번 호출
    elif n == 1:
        memo[n] = [0, 1]  # 0이 0번, 1은 1번 호출
    else:
        minus1 = fibonacci(n - 1)
        minus2 = fibonacci(n - 2)
        memo[n] = [minus1[0] + minus2[0], minus1[1] + minus2[1]]  # 각각 더해서 저장

    return memo[n]


# 테스트 케이스 입력
t = int(input())
for _ in range(t):
    n = int(input())
    result = fibonacci(n)
    print(result[0], result[1])  # 0이 몇 번, 1이 몇 번 호출됐는지 출력
