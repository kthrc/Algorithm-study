def solution(phone_number):
    answer = ''
    
    # 마스킹할 부분 자르기
    front = phone_number[:-4]
    rear = phone_number[-4:]
    
    # 개수만큼 *로 마스킹
    for n in list(front):
        answer += '*'
        
    # 뒷4자리 합치기
    answer += rear
    
    return answer