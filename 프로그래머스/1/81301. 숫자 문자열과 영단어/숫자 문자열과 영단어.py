def solution(s):
    answer = ''
    box = ''
    
    # 영단어-숫자 매칭
    num_dict = {"zero" : '0', "one" : '1', "two": '2',
                "three" : '3', "four" : '4', "five" : '5',
                "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'}
    
    for ch in s:
        
        # 정수 처리
        if ch.isdigit() == True:
            answer += ch
        # 문자 처리
        else:
            # 문자 적립(완성 X)
            box += ch
            
            # 문자 완성
            if box in num_dict:
                answer += num_dict[box]
                box = ''
                
         
    return int(answer)