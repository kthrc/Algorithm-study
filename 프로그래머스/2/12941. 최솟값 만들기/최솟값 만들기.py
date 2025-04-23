def solution(A, B):
    A.sort()  # A는 오름차순 정렬
    B.sort(reverse=True)  # B는 내림차순 정렬
    answer = sum(a * b for a, b in zip(A, B))  # 각 요소를 곱해서 더하기
    return answer