# M과 N 입력받기
m = int(input())
n = int(input())

arr = []
# m과 n 사이에서 소수를 찾는 함수
def sosu(m, n, arr):
    while m <= n:
        temp_arr = []
        for i in range(m):
            if m % (i+1) == 0:
                temp_arr.append(i)
        if len(temp_arr) == 2:
            arr.append(m)
        m += 1
    return arr

# 함수 호출 및 이하 계산 이후, 출력
arr = sosu(m, n, arr)

if len(arr) != 0:
    # 소수의 합 출력
    total = 0
    for i in arr:
        total += i
    print(total)
    # 소수 중 최솟값을 출력
    print(arr[0])
else:
    print(-1)