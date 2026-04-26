import sys
input = sys.stdin.readline

n = int(input())
weights = [0] * 26  # A~Z

for _ in range(n):
    word = input().strip()
    length = len(word)
    
    for i in range(length):
        char = word[i]
        weights[ord(char) - ord('A')] += 10 ** (length - i - 1)

# 가중치 정렬 (큰 순)
weights.sort(reverse=True)

num = 9
answer = 0

for w in weights:
    if w == 0:
        break
    answer += w * num
    num -= 1

print(answer)