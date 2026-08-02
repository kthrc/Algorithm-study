def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        cnt = divisor_count(i)

        if cnt > limit:
            answer += power
        else:
            answer += cnt

    return answer

def divisor_count(number):
    count = 0

    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            if i == number // i:
                count += 1
            else:
                count += 2

    return count