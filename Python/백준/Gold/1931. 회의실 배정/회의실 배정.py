import sys
input = sys.stdin.readline

n  = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key=lambda x: (x[1], x[0]))

fin = 0
cnt = 0
for i in arr:
    if i[0] >= fin:
        cnt += 1
        fin = i[1]

print(cnt)
