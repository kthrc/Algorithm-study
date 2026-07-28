from itertools import combinations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    # print(list(combinations(nums, 3)))
    
    for l in list(combinations(nums, 3)):
        if is_prime(sum(l)) == True:
            answer += 1
    
    return answer