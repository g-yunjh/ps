import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

min_num = float('inf')
i = 0
for j in range(n):
    while (i <= j) and (arr[j] - arr[i] >= m):
        min_num = min(min_num, arr[j] - arr[i])
        i+=1

print(min_num)