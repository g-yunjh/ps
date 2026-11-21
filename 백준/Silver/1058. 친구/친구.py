n = int(input())

arr = []
for i in range(n):
    arr.append(list(input()))

tmp = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == "Y":
            tmp[i].append(j)

ans = 0
for i in range(n):
    tmp2 = tmp[i].copy()
    for j in tmp[i]:
        tmp2 += tmp[j]
    tmp2 = set(tmp2)
    ans = max(ans, len(tmp2) - 1)
print(ans)
