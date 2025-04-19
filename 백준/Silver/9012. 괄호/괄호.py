# 입력 받기
n = int(input())

lines = []
for i in range(n):
    line = input()
    lines.append(line)
# print(lines)

# 예외 처리
for line in lines:
    if(len(line) == 0 or len(line) % 2 == 1 or line[0] == ')' or line[len(line)-1] == '('):
        print("NO")
        continue

    # 반복문 돌 때마다 stack 비워줘야함
    stack = []
    for ch in line:
        if(ch == '('):
            # 여는 괄호면 스택에 추가
            stack.append('C')
        else:
            # 닫는 괄호일 때 처리
            # 1. 스택 비었으면 NO\
            if not stack:
                print("NO")
                break
            # 2. 아니면 스택에서 pop
            stack.pop()

    # for .. else 문 사용 -> for문을 다 돌고 이상이 없었을 때
    else:
        if not stack:
            print("YES")
        else:
            print("NO")