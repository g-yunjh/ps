from itertools import combinations

n, m = map(int, input().split())

arr = [i+1 for i in range(n)]
ans = list(combinations(arr, m))
for i in ans:
    for j in i:
        print(j, end = " ")
    print()