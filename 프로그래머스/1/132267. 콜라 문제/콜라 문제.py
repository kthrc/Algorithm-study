def solution(a, b, n):
    answer = 0
    
    while (n // a > 0):
        # 콜라병 교환받은 값(by 마트)
        change = (n // a) * b
        # 총 콜라병 개수
        n = (n % a) + change
        # 받았었던 콜라 누적 합
        answer += change
    
    return answer