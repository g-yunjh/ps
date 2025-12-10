import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

tmp = 0
for i in range(x):
    tmp += arr[i]
max_num = tmp

cnt = 1
for i in range(n - x):
    tmp -= arr[i]
    tmp += arr[x + i]
    if (tmp > max_num):
        max_num = tmp
        cnt = 1
    elif (tmp == max_num):
        cnt += 1

if (max_num == 0):
    print("SAD")
else:
    print(max_num)
    print(cnt)
