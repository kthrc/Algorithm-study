from itertools import permutations

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    checked = []  # 이미 검사한 숫자 저장

    # 1자리 ~ 전체 자리 수까지 순열 생성
    for r in range(1, len(numbers) + 1):
        perm = permutations(numbers, r)

        for p in perm:
            num = int(''.join(p))  # 조합을 정수로 변환

            if num not in checked:  # 중복 제거
                checked.append(num)

                if is_prime(num):  # 소수이면 정답에 +1
                    answer += 1

    return answer
