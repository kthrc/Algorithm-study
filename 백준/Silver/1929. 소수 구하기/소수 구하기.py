# 범위 입력받기
n, m = map(int, input().split())

# depth1: numerator
for i in range(n, m+1):
    # 소수 조건: 2 이상
    if(i == 1):
        continue
    # depth2: denominator
    for j in range(2, int(i**0.5)+1):
        if (i % j == 0):
            break
    else:
        print(i)
       
