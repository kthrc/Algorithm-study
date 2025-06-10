from collections import deque  # 덱 사용

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2

    if total % 2 != 0:  # 전체 합이 홀수면 불가능
        return -1

    target = total // 2
    count = 0
    max_count = len(q1) * 4  # 횟수 제한

    while count <= max_count:
        if sum1 == target:  # 합 맞으면 종료
            return count
        if sum1 > target:  # 큐1이 크면 -> 큐2로 이동
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        else:  # 큐2가 크면 -> 큐1로 이동
            num = q2.popleft()
            q1.append(num)
            sum2 -= num
            sum1 += num
        count += 1

    return -1  # 제한 초과 시 실패