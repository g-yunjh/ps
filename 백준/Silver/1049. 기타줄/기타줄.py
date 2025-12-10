import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

six = []
one = []

for _ in range(m):
    a, b = map(int, input().split())
    six.append(a)
    one.append(b)

min_six = min(six)
min_one = min(one)

print(min(n//6*min_six + n%6*min_one, min_one * n, math.ceil(n/6)*min_six))
