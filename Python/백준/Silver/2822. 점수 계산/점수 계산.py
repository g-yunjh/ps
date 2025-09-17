import sys
input = sys.stdin.readline

arr = []
for i in range(8):
    k = int(input())
    arr.append([k, i+1])

arr.sort(key = lambda x : x[0], reverse=True)
arr = arr[0:5]
arr.sort(key = lambda x : x[1])

# 총합 출력
total = 0
for i in arr:
    total += i[0]
print(total)

# 순서대로 출력
for i in arr:
    print(i[1], end = " ")
