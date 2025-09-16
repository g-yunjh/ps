import sys
input = sys.stdin.readline

n = int(input())
arr = []
ans = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    ans.append(cnt + 1)

for i in ans:
    print(i, end = " ")
    