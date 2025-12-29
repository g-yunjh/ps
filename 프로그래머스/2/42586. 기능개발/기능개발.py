import math

def solution(progresses, speeds):
    # 각 작업이 며칠 걸리는지 계산
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    answer = []
    max_day = days[0]
    count = 0
    
    for day in days:
        if day <= max_day:
            count += 1
        else:
            answer.append(count)
            max_day = day
            count = 1
    answer.append(count)
    return answer