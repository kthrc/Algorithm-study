def solution(s):
    answer = []
    last = {}

    for i, ch in enumerate(s):
        if ch in last:
            answer.append(i - last[ch])
        else:
            answer.append(-1)

        last[ch] = i

    return answer