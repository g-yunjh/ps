h, m = map(int, input().split(" "))
n = int(input())

if m + n >= 60:
    if (m+n)//60 + h > 23:
        print((m+n)//60 + h - 24, (m+n)%60)
    else:    
        print((m+n)//60 + h, (m+n)%60)
else:
    print( h, m+n )
