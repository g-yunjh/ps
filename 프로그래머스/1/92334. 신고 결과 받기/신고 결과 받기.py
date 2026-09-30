def solution(id_list, report, k):
    report = list(set(report))
    
    # 신고당한 횟수 카운트
    cnt = {}
    for i in id_list:
        cnt[i] = 0
    for i in report:
        cnt[i.split()[1]] += 1
        
    # 누가 정지된걸까
    arr1 = []
    for i in cnt:
        if cnt[i] >= k:
            arr1.append(i)
    
    # 정지시킨 ID 갯수 카운트
    cnt = {}
    for i in id_list:
        cnt[i] = 0
    for i in report:
        tmp1 = i.split()[0]
        tmp2 = i.split()[1]
        if tmp2 in arr1:
            cnt[tmp1] += 1
    return list(cnt.values())
    