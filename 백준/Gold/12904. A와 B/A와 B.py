def MakeSToT(S, T):
    # T -> S 로 변환
    while len(T) > len(S):
        # A로 끝나면 -> A 제거
        if T[-1] == 'A':
            T = T[:-1]
        else:
            # B 제거
            T = T[:-1]
            # 문자열 뒤집기
            T = T[::-1]

    if S == T:
        return 1
    else:
        return 0
    
S = input().strip()
T = input().strip()

print(MakeSToT(S,T))