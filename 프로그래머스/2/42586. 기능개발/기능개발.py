import math
def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range(len(progresses)):
        # 남은 일수 차례로 일단 계산
        day = math.ceil((100 - progresses[i]) / speeds[i])
        # 배열에 값 추가
        days.append(day)
    
    # 기준일
    standard_day = days[0]
    # 첫번째 기능 실행 -> 1부터 시작
    count = 1
    
    for i in range(1, len(days)):
        # 기준일 미만이면 귀속됨(개수 추가)
        if days[i] <= standard_day:
            count += 1
        else:
            answer.append(count)
            standard_day = days[i]
            # 본인을 포함하여 반복문 다시 돌리기 -> 1부터 시작(기준점 변경)
            count = 1
        
    # 마지막 값까지 추가
    answer.append(count)
    
    return answer