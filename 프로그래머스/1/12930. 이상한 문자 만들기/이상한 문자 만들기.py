def solution(s):
    answer = ''
    idx = 0
    
    for ch in s:
        # 공백 처리
        if ch == ' ': 
            idx = 0
            answer += ' '
        else:
            if idx % 2 == 0:
                answer += ch.upper()
            else:
                answer += ch.lower()
            idx += 1
    
    return answer