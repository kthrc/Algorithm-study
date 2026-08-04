def solution(n):
    if n == 1:
        return 1

    first = 1   # 1칸
    second = 2  # 2칸

    for _ in range(3, n + 1):
        first, second = second, (first + second) % 1234567

    return second