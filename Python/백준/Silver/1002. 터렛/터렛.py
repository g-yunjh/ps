import sys
input = sys.stdin.readline

t = int(input())
answer = []

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d2 = (x2 - x1)**2 + (y2 - y1)**2
    s_plus = (r1 + r2)**2
    s_minus = (r1 - r2)**2

    if d2 == 0 and r1 == r2:
        answer.append(-1)
    elif d2 == 0 and r1 != r2:
        answer.append(0)
    elif d2 == s_plus:
        answer.append(1)   # 외접
    elif d2 > s_plus:
        answer.append(0)   # 서로 떨어짐
    elif d2 == s_minus:
        answer.append(1)   # 내접
    elif d2 < s_minus:
        answer.append(0)   # 내포
    else:
        answer.append(2)   # 두 점에서 만남

for v in answer:
    print(v)
