def is_Valid(s):
    stack = []
    for ch in s:
        # 여는 괄호면
        if ch in '({[':
            stack.append(ch)
        # 닫는 괄호면
        else:
            #  닫는 괄호인데 스택 비어있으면
            if not stack:
                return False
            # 괄호 처리
            top = stack.pop()
            
            if ch == ')' and top != '(':
                return False
            elif ch == '}' and top != '{':
                return False
            elif ch == ']' and top != '[':
                return False
            
    return len(stack) == 0
            
def solution(s):
    answer = -1
    count = 0
    for i in range(len(s)):
        # 회전
        rotated = s[i:] + s[:i]
        # print(rotated)
        
        if(is_Valid(list(rotated))):
            count += 1
    
    return count