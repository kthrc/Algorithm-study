def solution(s, bomb):
    stack = []

    for ch in s:
        # 스택에 글자 추가
        stack.append(ch)

        # 문자열 안에 폭탄문자열 여부 확인
        if ''.join(stack[-len(bomb):]) == bomb:
            del stack[-len(bomb):]

    # 결과 합치기
    rslt = ''.join(stack)

    if not rslt:
        return "FRULA"
    else:
        return rslt
            
s = input().strip()
bomb = input().strip()

print(solution(s, bomb))