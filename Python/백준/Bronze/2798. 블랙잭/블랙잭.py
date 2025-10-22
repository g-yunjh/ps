import sys
input = sys.stdin.readline

# input
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# process
arr.sort()
hap = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            hap.append(arr[i] + arr[j] + arr[k])

hap.sort(reverse=True)
for i in hap:
    if (i <= m):
        print(i)
        break
