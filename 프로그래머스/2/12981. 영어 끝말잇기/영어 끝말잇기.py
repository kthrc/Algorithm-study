def solution(n, words):

    for i in range(1, len(words)):
        
        # 끝 알파벳 - 다음 단어 첫 알파벳 매치 x
        if words[i-1][-1] != words[i][0]:
            return [(i%n+1), (i//n+1)]
            
        # 중복 단어인 경우
        for j in range(i):
            if words[i] == words[j]:
                return [(i%n+1),(i//n+1)]
        
    # 탈락자가 생기지 않는 경우
    return [0,0]