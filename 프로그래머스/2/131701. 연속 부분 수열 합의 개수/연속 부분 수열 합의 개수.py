def solution(elements):
    sums = set()
    n = len(elements)
    
    circle = elements * 2
    
    for length in range(1, n + 1):
        for start in range(n):
            sums.add(sum(circle[start:start + length]))
    
    return len(sums)