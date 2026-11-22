n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = []
if len(arr) % 2 != 0:
    result.append(arr[-1])
    arr.pop()
start = 0
end = len(arr)
while start < end:
    result.append(arr[start]+arr[end-1])
    start += 1
    end -= 1
print(max(result))