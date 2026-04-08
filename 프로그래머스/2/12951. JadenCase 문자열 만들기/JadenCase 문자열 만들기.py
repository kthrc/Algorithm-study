def solution(s):
    answer = ''
    word_list = []
    # 공백 기준으로 분리
    word_list = s.split(' ')

    
    for word in word_list:
        # 앞/뒷 단어 분리
        first_word = word[:1]
        rest = word[1:]
        
        if first_word >= 'a' and first_word <= 'z':
            first_word = first_word.upper()
        
        # 첫 글자 제외하고 이어지는 알파벳 소문자
        rest = rest.lower()
        
        answer += first_word + rest + ' '
    # 마지막 공백 제거
    return answer[:-1]