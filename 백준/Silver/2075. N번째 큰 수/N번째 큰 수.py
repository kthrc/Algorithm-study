import heapq

n = int(input())
heap = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > n:
            heapq.heappop(heap)

print(heap[0])
