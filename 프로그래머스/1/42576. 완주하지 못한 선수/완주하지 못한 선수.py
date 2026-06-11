def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    # completion의 길이만큼 비교
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i] # 달라지는 순간 그 사람이 범인
            
    # 반복문이 다 끝났는데도 안 걸렸다면, 정렬 후 맨 마지막에 있는 사람이 범인
    return participant[-1]