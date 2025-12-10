total = 0
arr = []

for i in range(9):
    n = int(input())
    arr.append(n)
    total += n

# 두 명의 합이 total - 100인 경우 찾기
found = False
for i in range(9):
    for j in range(i + 1, 9):
        if total - (arr[i] + arr[j]) == 100:
            # 제외할 두 명 저장
            a, b = arr[i], arr[j]
            found = True
            break
    if found:
        break

# 두 명 제외하고 나머지 출력
arr.remove(a)
arr.remove(b)
arr.sort()

for h in arr:
    print(h)
