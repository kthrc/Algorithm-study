from collections import deque

def AC(commands,array_num,array):
    
    is_reversed = False # flag(Reverse)
    
    for cmd in commands:
        if cmd == 'R':
            is_reversed = not is_reversed # T/F 상관없이 변경할 수 있도록 설정
            
            
        elif cmd == 'D':
            # 배열: 공백
            if not array:
                return "error" # 종료
            # 배열 not 공백
            else:
                # 뒤집혔으면 pop
                if is_reversed == True:
                    array.pop()
                else:
                    array.popleft()
                    

    # 결과적으로 뒤집혔는지 최종 확인
    if is_reversed == True:
        array.reverse()
            

    return '[' + ','.join(array) + ']' # list 형태로 출력



cnt = int(input().split()[0])

for _ in range(cnt):
    commands = input().strip()
    array_num = int(input().strip())
    array_str = input().strip() # array -> str이므로 [] , 처리 필요
    
    if array_str == "[]":
        array = deque()
    else:
        array = deque(array_str[1:-1].split(','))
    
    print(AC(commands,array_num,array))
