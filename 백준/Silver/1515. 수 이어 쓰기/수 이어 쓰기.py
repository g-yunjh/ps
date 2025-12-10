import sys

S = sys.stdin.readline().strip()
n = 1
i = 0  # S에서 현재 확인 중인 위치

while i < len(S):
    for digit in str(n):   # n의 각 자릿수를 확인
        if S[i] == digit:
            i += 1
            if i == len(S):
                break
    n += 1

print(n - 1)
