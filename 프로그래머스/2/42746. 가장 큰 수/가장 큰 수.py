def solution(numbers):
    arr0 = []
    for n in numbers:
        arr0.append(str(n) * 3)
    arr0.sort(reverse = True)
    
    arr1 = []
    for i in arr0:
        arr1.append(i[:len(i)//3])
    
    ans = "".join(arr1)
    if ans[0] == "0":
        return str(int(ans))
    else:
        return ans    
        