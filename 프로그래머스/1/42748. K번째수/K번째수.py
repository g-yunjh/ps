def solution(array, commands):
    ans = []
    for c in commands:
        arr = array[c[0]-1:c[1]]
        arr.sort()
        ans.append(arr[c[2]-1])
    return ans
        