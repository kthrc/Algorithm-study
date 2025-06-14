# 가능한 모든 세 자리 숫자 만들기 (1~9, 중복 없는 숫자)
possible_list = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and i != k and j != k:
                possible_list.append([i, j, k])

# 질문 수 입력
n = int(input())

# 입력된 질문 처리
questions = []
for _ in range(n):
    number, strike, ball = map(int, input().split())
    questions.append((list(map(int, str(number))), strike, ball))

# 후보 중 조건을 만족하지 않는 숫자 제거
count = 0
for num in possible_list:
    is_possible = True

    for q_num, q_strike, q_ball in questions:
        strike = 0
        ball = 0

        for i in range(3):
            if num[i] == q_num[i]:
                strike += 1
            elif num[i] in q_num:
                ball += 1

        if strike != q_strike or ball != q_ball:
            is_possible = False
            break

    if is_possible:
        count += 1

print(count)
