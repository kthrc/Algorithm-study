# 값을 받아오기 위한 변수 선언
n,m = map(int, input().split())

# 팩토리얼 함수 
def fac(u):
    j = 1
    for i in range(2,u+1):
        j *= i
    return j

# combination 공식 적용 (n! / (m! * (n-m)!))
# 나눗셈 연산자 / 대신 // 적용 (버림 나눗셈 적용) -> 조합은 개수니까!
rslt = int(fac(n) // (fac(m) * fac(n-m)))

# 출력
print(rslt)