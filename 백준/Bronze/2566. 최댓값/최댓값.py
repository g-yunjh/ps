x = []
max = 0
max_loc = []

for row in range(9):
    i = list(map(int, input().split()))
    x.append(i)

for row in range(9):
    for col in range(9):
        if x[row][col] >= max:
            max = x[row][col]
            max_loc = [row+1, col+1]

print(max)
print(max_loc[0], max_loc[1])