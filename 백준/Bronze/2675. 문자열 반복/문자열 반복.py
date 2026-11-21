t = int(input())
i = 0
while i < t:
    i = i+1
    r, s = input().split(" ")
    for c in s:
        print(c*int(r), end='')
    print()

