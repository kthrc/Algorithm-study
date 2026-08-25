def solution(s):
    count = 0      
    zero_count = 0  
    
    while s != "1":
        zero_count += s.count("0")
        
        one_count = s.count("1")
        s = bin(one_count)[2:]
        
        count += 1
    
    return [count, zero_count]