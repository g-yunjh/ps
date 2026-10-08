def solution(files):
    arr = [[i] for i in range(len(files))]
    for i in range(len(files)):
        tmp = ""
        ch = 0
        for j in files[i]:
            if ch == 0 and '0' <= j <= '9':
                ch += 1
                arr[i].append(tmp.lower())
                tmp = j
            elif ch == 1 and (j > '9' or j < '0'):
                ch += 1
                arr[i].append(int(tmp))
                tmp = j
            else:
                tmp += j
        if ch == 2:
            arr[i].append(tmp)
        else:
            arr[i].append(int(tmp))
            arr[i].append("")
    arr.sort(key = lambda x: (x[1], x[2], x[0]))
    
    ans = []
    for i in arr:
        ans.append(files[i[0]])
    return ans
                