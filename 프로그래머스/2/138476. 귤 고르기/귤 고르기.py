def solution(k, tangerine):
    answer = 0
    dic = {}

    # 귤 크기별 개수 세기
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1

    # 개수만 내림차순 정렬
    counts = sorted(dic.values(), reverse=True)

    # 많은 종류부터 선택
    for count in counts:
        k -= count
        answer += 1

        if k <= 0:
            break

    return answer