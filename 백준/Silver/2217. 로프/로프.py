import sys
input = sys.stdin.readline

n = int(input())
w_list = []
for i in range(n):
    w = int(input())
    w_list.append(w)

w_list.sort(reverse=True)

# greedy
m = 0
for i, w in enumerate(w_list, start=1):
    m = max(m, i * w)

print(m)