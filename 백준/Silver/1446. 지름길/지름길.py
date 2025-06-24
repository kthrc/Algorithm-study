n, meter = map(int, input().split())

shortcuts = []

for _ in range(n):
    start, end, length = map(int, input().split())
    
    # end > meter -> 저장 X
    if end > meter:
        continue
    shortcuts.append((start, end, length))
    
# dp 생성
dp = [i for i in range(meter + 1)]

for i in range(meter + 1):
    # 일반 도로
    if i + 1 <= meter:
        if dp[i + 1] > dp[i] + 1:
            dp[i + 1] = dp[i] + 1

    # 지름길 있는지 확인
    for start, end, length in shortcuts:
        if start == i:
            # 지름길 확인 후 업데이트
            if dp[end] > dp[start] + length:
                dp[end] = dp[start] + length

print(dp[meter])

