# 모듈러 거듭제곱
def solution(A, B, C):
    return pow(A,B,C)

A, B, C = map(int, input().split(' '))
print(solution(A,B,C))