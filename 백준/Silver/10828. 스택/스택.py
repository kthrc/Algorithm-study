n = int(input())
stack = []
output = []  # 출력 결과를 담을 리스트

for _ in range(n):
    line = input().split()

    if line[0] == 'push':
        stack.append(int(line[1]))

    elif line[0] == 'pop':
        if stack:
            output.append(str(stack.pop()))
        else:
            output.append("-1")

    elif line[0] == 'size':
        output.append(str(len(stack)))

    elif line[0] == 'empty':
        output.append("0" if stack else "1")

    elif line[0] == 'top':
        if stack:
            output.append(str(stack[-1]))
        else:
            output.append("-1")

# 출력 결과를 한 번에 출력
print("\n".join(output))
