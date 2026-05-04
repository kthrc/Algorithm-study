def solution(array, commands):
    
    answer = []
    for cmd in commands:
        i, j, k = cmd # commands의 [2,5,3] 할당
        sliced = array[i-1:j] # 자르기
        sliced.sort() # 정렬
        answer.append(sliced[k-1])
        
    return answer