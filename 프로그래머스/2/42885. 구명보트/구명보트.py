def solution(people, limit):
    people.sort(reverse = True)
    l = len(people) - 1
    h = 0
    cnt = 0
    while h <= l:
        if people[h] + people[l] <= limit:
            cnt += 1
            h += 1
            l -= 1
        else:
            cnt += 1
            h += 1
    return cnt
        