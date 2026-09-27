def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    dic1 = {}
    for i in range(1, len(str1)):
        if "a" <= str1[i-1] <= "z" and "a" <= str1[i] <= "z":
            tmp = str1[i-1] + str1[i]
            if tmp in dic1:
                dic1[tmp] += 1
            else:
                dic1[tmp] = 1
    dic2 = {}
    for i in range(1, len(str2)):
        if "a" <= str2[i-1] <= "z" and "a" <= str2[i] <= "z":
            tmp = str2[i-1] + str2[i]
            if tmp in dic2:
                dic2[tmp] += 1
            else:
                dic2[tmp] = 1
    
    # min
    tmp = []
    for i in dic1:
        if i in dic2:
            tmp.append(min(dic1[i], dic2[i]))
    min_num = sum(tmp)
        
    # max
    tmp = []
    for i in dic1:
        if i in dic2:
            tmp.append(max(dic1[i], dic2[i]))
        else:
            tmp.append(dic1[i])
    for i in dic2:
        if i not in dic1:
            tmp.append(dic2[i])
    max_num = sum(tmp)
    
    if max_num == 0:
        result = 1
    else:
        result  = min_num / max_num
    return int(result * 65536)