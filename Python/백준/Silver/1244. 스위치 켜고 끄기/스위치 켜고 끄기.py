import sys
input = sys.stdin.readline

def turn(arr, i):
    if arr[i] == 0:
        arr[i] = 1
    else:
        arr[i] = 0

switch = int(input())
arr = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(switch):
            if (i + 1) % num == 0:
                turn(arr, i)
    elif sex == 2:
        idx = num - 1
        turn(arr, idx)
        k = 1
        while idx - k >= 0 and idx + k < switch and arr[idx - k] == arr[idx + k]:
            turn(arr, idx - k)
            turn(arr, idx + k)
            k += 1

for i in range(switch):
    print(arr[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
