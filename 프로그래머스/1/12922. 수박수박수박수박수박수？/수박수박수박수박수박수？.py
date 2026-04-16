def solution(n):
    answer_list = []
    for i in range(1,n+1):
        if i % 2 == 1:
            answer_list.append("수")
        else:
            answer_list.append("박")
    
    answer = ''.join(answer_list)
    return answer