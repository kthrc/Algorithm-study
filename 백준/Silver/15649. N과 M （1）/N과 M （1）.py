# 입력 받기
n,m = list(map(int,input().split()))
 
s = []

# dfs(depth first search)
def dfs():
    # 출력 관련
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            # 반복문 돌려서 없는 요소 찾으면 다시 추가
            s.append(i)
            # 재귀 호출
            dfs()
            # 재귀 호출이 끝나면 마지막에 넣은 숫자 제거 -> 백트래킹
            s.pop()
 
dfs()