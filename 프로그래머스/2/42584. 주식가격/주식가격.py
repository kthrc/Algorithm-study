def solution(prices):
    stack = []
    # 이중 반복문
    for i in range(len(prices)):
        # depth 2 반복문 끝나면 second 0으로 초기화
        second = 0
        # 배열의 다음 원소와 비교하면서
        for j in range(i+1, len(prices)):
            # 반복문 돌면서 배열의 다음 원소보다 작지 않으면 +1(초 단위)
            second += 1
            # 다음 원소가 더 작으면 depth 2 종료
            if(prices[i] > prices[j]):
                break
        # 초 계산 후 스택에 추가
        stack.append(second)
                        
    return stack