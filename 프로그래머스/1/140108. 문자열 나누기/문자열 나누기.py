def solution(s):
    answer = 0
    x = ''
    same = 0
    diff = 0

    for ch in s:
        if same == 0 and diff == 0:
            x = ch

        if ch == x:
            same += 1
        else:
            diff += 1

        if same == diff:
            answer += 1
            same = 0
            diff = 0

    if same != 0 or diff != 0:
        answer += 1

    return answer