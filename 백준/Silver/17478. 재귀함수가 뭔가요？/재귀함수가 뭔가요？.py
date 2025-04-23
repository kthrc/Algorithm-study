n = int(input())
output = ['어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.']

underline = 0

def recursion(n):
    global underline
    if(n == 0):
        output.append('____'*(underline)+'"재귀함수가 뭔가요?"')
        output.append('____'*(underline)+'"재귀함수는 자기 자신을 호출하는 함수라네"')
        output.append('____'*(underline)+"라고 답변하였지.")
        return # 종료

    if(n >= 1):
        output.append('____'*(underline)+'"재귀함수가 뭔가요?"')
        output.append('____'*(underline)+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        output.append('____'*(underline)+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        output.append('____'*(underline)+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        
        underline += 1  # 재귀 들어가기 전에 증가!
        recursion(n - 1)
        underline -= 1  # 돌아오면 줄여줘야 이전 깊이로 복원됨

        output.append('____' * underline + "라고 답변하였지.")



recursion(n)

for i in output:
    print(i)