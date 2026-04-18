def solution(new_id):
    answer = ''
    # 1단계: 소문자 치환
    new_id = new_id.lower()
    
    # 2단계: 허용문자만 남김
    for ch in new_id:
        if ch.islower() or ch.isdigit() or ch in ['-', '_', '.']:
            answer += ch
        
    # 3단계: ..(2번이상) -> . 치환
    temp = ''
    for ch in answer:
        if not (temp and temp[-1] == '.' and ch == '.'):
            temp += ch
    answer = temp
    
    # 4단계: .~~. -> ~~ 
    answer = answer.strip('.')
    
    # 5단계: '' -> a
    if answer == '':
        answer = 'a'
        
    # 6단계: 문자 15개 초과 -> 첫 15개의 문자만 남기기
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')

    # 7단계: 2자 이하 -> 마지막 문자의 길이가 3이 될 때까지 반복
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer