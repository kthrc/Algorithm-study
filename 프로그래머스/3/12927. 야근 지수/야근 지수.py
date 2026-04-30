import heapq
def solution(n, works):

    if sum(works) <= n:
        return 0
    else:
        works = [-w for w in works] # heapq는 최소 힙 -> (-)연산으로 최대 힙 만들기
        heapq.heapify(works) # 리스트를 즉각적으로 heap으로 변환함
        
        for _ in range(n):
            biggest = heapq.heappop(works) # heapq는 최솟값을 꺼냄
            biggest += 1 # 문제에서는 -1 -> 코드에서는 +1
            heapq.heappush(works, biggest) # +1 결과물을 heap에 추가
            
    return sum([w ** 2 for w in works])
        
        
#     # 남은 작업량 X
#     if sum(works) - n <= 0:
#         return 0
#     # 남은 작업량 O
#     else: 
#         for _ in range(n):
#             idx = works.index(max(works))
#             works[idx] -= 1


#         # 작업량 제곱
#         for i in range(len(works)):
#             works[i] = pow(works[i], 2)
    
#     # 제곱합 출력
#     return sum(works)

# 힙은 특정한 규칙을 가지는 트리
# 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리 