s = input()
t = len(s)
n = 1

for i in range(t):
    if s[i] != s[t-i-1]:
        n = 0
        break

print(n)
