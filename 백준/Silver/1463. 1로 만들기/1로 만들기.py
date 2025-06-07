n = int(input()) 

memo = [0] * (n + 1)

for i in range(2, n + 1):
    # 기본값 (1 빼기)
    memo[i] = memo[i - 1] + 1

    # 2로 나눠지는 경우
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1)

    # 3으로 나눠지는 경우
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1)

print(memo[n])
