def solution(s):
    
    answer = ''
    s = list(map(int,s.split()))
   
    maxv = max(s)
    minv = min(s)
    
    answer = str(minv) + " " + str(maxv)
    
    return answer