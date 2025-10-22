import sys
input = sys.stdin.readline
import math

n = int(input())
arr = list(map(int, str(n)))

for i in range(len(arr)):
    if (arr[i] == 6):
        arr[i] = 9 # 모든 6을 9로 만들어주기

arr.sort()
max_cnt = 1
cnt = 1
cnt_9 = 0

if (arr[0] == 9):
    cnt_9 += 1
for i in range(1,len(arr)):
    if (arr[i] == 9):
        cnt_9 += 1
    elif (arr[i] == arr[i-1]):
        cnt += 1
        if (max_cnt < cnt):
            max_cnt = cnt
    else:
        # 초기화
        cnt = 1

ans = max(max_cnt, math.ceil(cnt_9/2))
print(ans)