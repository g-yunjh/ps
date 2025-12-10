import sys
input = sys.stdin.readline

t = int(input())
ans = []
for i in range(t):
    arr = []
    n = True
    txt = str(input())
    for j in txt:
        if j == '(':
            arr.append(1)
        elif j == ')':
            if len(arr) == 0:
                ans.append("NO")
                n = False
                break
            else:
                arr.pop()
    if len(arr) == 0 and n == True:
        ans.append("YES")
    elif n == True:
        ans.append("NO")

for i in ans:
    print(i)
    