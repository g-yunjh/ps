def solution(numbers):
    arr = [str(n)*3 for n in numbers]
    arr.sort(reverse = True)
    ans = ""
    for i in arr:
        ans += i[:len(i)//3]
    if ans[0] == '0':
        return '0'
    return ans
