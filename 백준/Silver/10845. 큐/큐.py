from collections import deque

# 입력 받기
n = int(input())
# 덱 함수 사용
queue = deque()
output = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        output.append(queue.popleft() if queue else '-1')
    elif cmd[0] == 'size':
        output.append(str(len(queue)))
    elif cmd[0] == 'empty':
        output.append('0' if queue else '1')
    elif cmd[0] == 'front':
        output.append(queue[0] if queue else '-1')
    elif cmd[0] == 'back':
        output.append(queue[-1] if queue else '-1')

print('\n'.join(output))
