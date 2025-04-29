# 기타 개수 입력 받기
n = int(input())
guitars = []
# 기타 시리얼 넘버 입력받기
for i in range(n):
    guitars.append(input())

# 자릿수 합계 함수
def digit_sum(s):
    total = 0
    for ch in s:
        if ch.isdigit():
            total += int(ch)
    return total

     
# 복합 기준 정렬 key=lambda x: (길이, 자릿수 합계 함수, 알파벳 순서)
guitars.sort(key=lambda x: (len(x), digit_sum(x), x))

for guitar in guitars:
    print(guitar)