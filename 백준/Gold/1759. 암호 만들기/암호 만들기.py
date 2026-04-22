from itertools import combinations

def MakingCode(L, C, chars):
    chars = sorted(chars)
    # print(chars)
    vowels = ['a', 'e', 'i', 'o', 'u']

    for comb in combinations(chars, L):
        v_count = 0 # 모음 개수
        c_count = 0 # 자음 개수

        for ch in comb:
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1

        if v_count >= 1 and c_count >= 2:
            print(''.join(comb)) # 리스트를 문자열로 재조합해서 출력
        
    

# 입력
L, C = map(int, input().split())

chars = input().split()

MakingCode(L, C, chars)
