import sys
input = sys.stdin.readline

n = int(input())
stack = []
max_num = 0
avail = True
answer = []
for _ in range(n):
    m = int(input())
    if max_num < m:
        for i in range(max_num + 1, m + 1):
            stack.append(i)
            answer.append('+')
        max_num = m

    if stack[-1] == m:
        stack.pop()
        answer.append('-')
    else:
        avail = False  

if avail == True:
    for i in answer:
        print(i)
else:
    print("NO")
 