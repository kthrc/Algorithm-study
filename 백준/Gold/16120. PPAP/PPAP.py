def MakePPAP(s):
    stack = []

    for ch in s:
        stack.append(ch)    
        if len(stack) >= 4 and "".join(stack[-4:]) == "PPAP":
            del stack[-3:]

    if stack == ["P"]:
        return "PPAP"
    else:
        return "NP"

        

s = input().strip()
print(MakePPAP(s))