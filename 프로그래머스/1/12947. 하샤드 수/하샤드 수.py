def solution(x):
    
    x_list = list(str(x))
    divisor = 0
    for ch in x_list:
        divisor += int(ch)
    
    if x % divisor == 0:
        return True
    else:
        return False