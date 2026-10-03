def solution(people, limit):
    people.sort(reverse = True)
    
    idx1 = 0
    idx2 = len(people) - 1
    cnt = 0
    while idx1 <= idx2:
        if (people[idx1] + people[idx2] <= limit):
            cnt += 1
            idx1 += 1
            idx2 -= 1
        else:
            cnt += 1
            idx1 += 1
    return cnt
            