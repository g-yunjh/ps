import sys
input = sys.stdin.readline

text = input().rstrip()
bomb = input().rstrip()

m = len(bomb)
last = bomb[-1]
bchars = list(bomb)

stack = []
for ch in text:
    stack.append(ch)
    if ch == last and len(stack) >= m and stack[-m:] == bchars:
        del stack[-m:]

result = ''.join(stack)
print("FRULA" if not result else result)
