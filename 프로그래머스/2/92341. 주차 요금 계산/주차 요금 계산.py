import math

def solution(fees, records):
    d1 = {}
    d2 = {} # 누적시간 관리할 딕셔너리
    
    for r in records:
        tmp = list(r.split())
        if tmp[2] == "IN":
            d1[tmp[1]] = tmp[0]
            if tmp[1] not in d2:
                d2[tmp[1]] = 0
        else:
            if int(d1[tmp[1]].split(":")[1]) <= int(tmp[0].split(":")[1]):
                d2[tmp[1]] += (int(tmp[0].split(":")[0]) - int(d1[tmp[1]].split(":")[0])) * 60
                d2[tmp[1]] += int(tmp[0].split(":")[1]) - int(d1[tmp[1]].split(":")[1])
            else:
                d2[tmp[1]] += (int(tmp[0].split(":")[0]) - int(d1[tmp[1]].split(":")[0]) - 1) * 60
                d2[tmp[1]] += int(tmp[0].split(":")[1]) - int(d1[tmp[1]].split(":")[1]) + 60
            d1[tmp[1]] = "23:59"
    
    # 최종적으로 출차되지 않은 차량
    for i in d1:
        if d1[i] != "23:59":
            d2[i] += (23 - int(d1[i].split(":")[0])) * 60
            d2[i] += 59 - int(d1[i].split(":")[1])
    
    result = list(d2.keys())
    result.sort()
    
    # 요금계산
    for i in d2:
        cnt = fees[1]
        if d2[i] > fees[0]:
            cnt += math.ceil((d2[i] - fees[0])/fees[2]) * fees[3]
        result[result.index(i)] = cnt
    return result
            
            
        