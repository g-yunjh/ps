def search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
ns = list(map(int, input().split()))
ns.sort()

m = int(input())
ms = list(map(int, input().split()))

for i in ms:
    if search(ns, i, 0, n-1) == True:
        print(1)
    else:
        print(0)
