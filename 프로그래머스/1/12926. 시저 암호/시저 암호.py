def solution(s, n):
    answer = ''
    
    for ch in s:
        # 공백
        if ch == ' ':
            answer += ' '
        
        # 소문자
        elif ch.islower():
            answer += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
        
        # 대문자
        else:
            answer += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
    
    return answer