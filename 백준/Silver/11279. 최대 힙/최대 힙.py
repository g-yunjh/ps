import heapq
import sys

input = sys.stdin.readline

n = int(input())

out = []
heap = []

for i in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            out.append(0)
        else:
            out.append(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)

for i in out:
    print(i)
    