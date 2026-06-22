def solution(answers):
    # 1번 수포자
    cnt1 = 0
    arr1 = [1,2,3,4,5]
    for i in range(len(answers)):
        k = i % 5
        if arr1[k] == answers[i]:
            cnt1 += 1
    # 2번 수포자
    cnt2 = 0
    arr2 = [2,1,2,3,2,4,2,5]
    for i in range(len(answers)):
        k = i % 8
        if arr2[k] == answers[i]:
            cnt2 += 1
    # 3번 수포자
    cnt3 = 0
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        k = i % 10
        if arr3[k] == answers[i]:
            cnt3 += 1
    
    # 결과 출력
    ans = []
    max_cnt = max(cnt1, cnt2, cnt3)
    if cnt1 == max_cnt:
        ans.append(1)
    if cnt2 == max_cnt:
        ans.append(2)
    if cnt3 == max_cnt:
        ans.append(3)
    
    return ans