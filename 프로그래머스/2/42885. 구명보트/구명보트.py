def solution(people, limit):
    people.sort(reverse = True)
    heavy = 0
    light = len(people) - 1
    ans = 0
    while heavy <= light:
        if people[heavy] + people[light] <= limit:
            ans += 1
            heavy += 1
            light -= 1
        else:
            ans += 1
            heavy += 1
    return ans