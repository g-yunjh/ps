def solution(s):
    groups = s[2:-2].split('},{')
    
    arr = []
    for group in groups:
        str_elements = group.split(',')

        int_elements = [int(x) for x in str_elements]
        
        cnt = len(int_elements)
        arr.append([cnt, int_elements])
        
    arr.sort(key = lambda x: x[0])
    
    ans = []
    for i in arr:
        for j in i[1]:
            if j not in ans:
                ans.append(j)
                
    return ans
            