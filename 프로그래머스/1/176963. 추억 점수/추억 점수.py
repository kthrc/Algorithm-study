def solution(name, yearning, photo):
    answer = []
    # 딕셔너리 생성
    matching = {}
    
    # 딕셔너리 매칭
    for i in range(len(name)):
        matching[name[i]] = yearning[i]
    
    for people in photo:
        score = 0
        
        for person in people:
            
            if person in matching:
                score += matching[person] # 딕셔너리 이용
                
        answer.append(score)
        
    
    return answer