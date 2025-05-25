def is_valid(s):
    stack = []
    for ch in s:
        if ch in '([{':  # 여는 괄호는 스택에 넣기
            stack.append(ch)
        else:  # 닫는 괄호인 경우
            if not stack:
                return False  # 스택이 비었으면 짝이 안 맞는 것
            top = stack.pop()
            # 닫는 괄호가 스택에서 꺼낸 괄호랑 짝이 안 맞으면 false
            if ch == ')' and top != '(':
                return False
            if ch == ']' and top != '[':
                return False
            if ch == '}' and top != '{':
                return False
    # 스택이 비어 있어야 올바른 괄호(0이면 true 아님 false)
    return len(stack) == 0

def rotate_string(s, i):
    result = ''
    length = len(s)
    for j in range(length):
        result += s[(i + j) % length]  # 회전된 문자열 만들기
    return result

def solution(s):
    count = 0
    for i in range(len(s)):
        rotated = rotate_string(s, i)  # 문자열 회전
        if is_valid(rotated):  # 올바른 괄호인지 확인
            count += 1
    return count
