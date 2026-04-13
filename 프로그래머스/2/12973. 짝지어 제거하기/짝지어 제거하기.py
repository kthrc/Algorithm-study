def solution(s):
    answer = -1

    # 공백 제거 strip()
    s = s.strip()
    s_list = list(s)
    
    # 반복되는 문자 제거
    # 스택
    stack = []
    
    for ch in s_list:
        if len(stack) == 0 or stack[-1] != ch:
            stack.append(ch)
            # print(stack)
        else:
            stack.pop()
            # print(stack)

    # 제거 결과 리턴
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
        
    return answer