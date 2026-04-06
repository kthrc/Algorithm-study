def solution(s, skip, index):
    answer = ''
#     s, skip 각각 쪼개서 리스트에 넣기: list()함수
    s_list = list(s)
    x_list = list(skip)
    combined = []
    
    for ch in s_list:
        origin = ord(ch) # 아스키코드 번호로 변경
        cnt = 0
        
        while cnt < index:
            
            origin += 1
            
            # z이상 처리
            if origin > ord('z'):
                origin = ord('a')
                
                
            # skip 처리
            if chr(origin) not in x_list:
                cnt += 1
                
        
        combined.append(chr(origin))
        
    answer = ''.join(combined)

    return answer