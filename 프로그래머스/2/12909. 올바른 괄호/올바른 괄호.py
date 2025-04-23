def solution(s):
    answer = True
    
    op = 0
    cl = 0
    tmp = 0
    
    for i in range(len(s)):
        if(s[i] == '('):
            op += 1
        else:
            cl += 1
            
        if(op < cl):
            return False
            
    # print(op, cl)
    if op != cl or s[0] == ')' or s[len(s)-1] == '(':
        return False
    return True
