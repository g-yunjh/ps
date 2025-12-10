# 수열 만들기
arr = []
for i in range(100):
    for j in range(i):
        arr.append(i)

# 구간 A, B 입력 받기
a, b = map(int, input().split())

# 반복문을 이용하여 구간의 합을 구하기
total = 0
for i in range(b):
    total += arr[i]

for i in range(a-1):
    total -= arr[i]

print(total)