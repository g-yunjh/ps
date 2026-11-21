str = input()
n = 0

for _ in str:
    if _ == 'A' or _ == 'B' or _ == 'C':
        n = n+3
    elif _ == 'D' or _ == 'E' or _ == 'F':
        n = n+4
    elif _ == 'G' or _ == 'H' or _ == 'I':
        n = n+5
    elif _ == 'J' or _ == 'K' or _ == 'L':
        n = n+6
    elif _ == 'M' or _ == 'N' or _ == 'O':
        n = n+7
    elif _ == 'P' or _ == 'Q' or _ == 'R' or _ == 'S':
        n = n+8
    elif _ == 'T' or _ == 'U' or _ == 'V':
        n = n+9
    elif _ == 'X' or _ == 'W' or _ == 'Y' or _=='Z':
        n = n+10
    else:
        n = n+11


print(n)