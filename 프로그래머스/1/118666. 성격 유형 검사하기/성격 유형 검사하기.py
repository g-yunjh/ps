def solution(survey, choices):
    arr = ""
    for i in range(len(choices)):
        if choices[i] > 4:
            arr += survey[i][1] * (choices[i] - 4)
        else:
            arr += survey[i][0] * -(choices[i] - 4)
    arr = list(arr)
    ch1 = {'R':0, 'T':0}
    ch2 = {'C':0, 'F':0}
    ch3 = {'J':0, 'M':0}
    ch4 = {'A':0, 'N':0}
    for i in arr:
        if i == 'R':
            ch1['R'] += 1
        elif i == 'T':
            ch1['T'] += 1
        elif i == 'C':
            ch2['C'] += 1
        elif i == 'F':
            ch2['F'] += 1
        elif i == 'J':
            ch3['J'] += 1
        elif i == 'M':
            ch3['M'] += 1
        elif i == 'A':
            ch4['A'] += 1
        else:
            ch4['N'] += 1
    
    ans = ''
    ans += sorted(ch1.items(), key = lambda x: x[1], reverse = True)[0][0]
    ans += sorted(ch2.items(), key = lambda x: x[1], reverse = True)[0][0]
    ans += sorted(ch3.items(), key = lambda x: x[1], reverse = True)[0][0]
    ans += sorted(ch4.items(), key = lambda x: x[1], reverse = True)[0][0]

    return ans
        