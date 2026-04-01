def solution(food):
    answer = ''
    f_answer = ''
    
    for i in range(1, len(food)):
        t = (food[i]//2)
        answer += str(i) * t
        
    f_answer = answer + '0' + answer[::-1]

    
    return f_answer