while True:
    n = int(input())
    x = []
    if n == -1:
        break
    else: 
        for i in range(1,n):
            if n%i == 0:
                x.append(i)
        if sum(x) == n:
            print(n , "=", end = ' ')
            for i in x:
                print(i, end = ' ')
                if i  == x[len(x)-1]:
                    break
                else:
                    print("+", end = ' ')
        else:
            print(n,"is NOT perfect.")
        