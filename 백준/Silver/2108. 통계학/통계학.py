import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

# 산술평균
print(round(sum(arr) / n))

# 중앙값
print(arr[n//2])

# 최빈값
prev_num = 0
cnt = 0
tmp = []
for i in range(n):
    if i == 0:
        prev_num = arr[0]
        cnt += 1
    elif arr[i] == prev_num:
        cnt += 1
        if i == n - 1:
            tmp.append([prev_num, cnt])
    else:
        tmp.append([prev_num, cnt])
        cnt = 1
        prev_num = arr[i]
tmp.sort(key  = lambda x: (-x[1], x[0]))

if n == 1:
    print(arr[0])
else:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])

# 범위
print(arr[-1] - arr[0])