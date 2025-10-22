import sys
input = sys.stdin.readline

# input
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# process
arr.sort()

ans = 0

s = 0
e = n-1
while (s < e):
    if (arr[s] + arr[e] == x):
        ans += 1
        s += 1
        e -= 1
    elif (arr[s] + arr[e] < x):
        s += 1
    else:
        e -= 1

print(ans)
