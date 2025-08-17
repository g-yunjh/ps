n = int(input())

out = []

stack = []
for i in range(n):
    command = input()
    if command == "pop":
        if len(stack) == 0:
            out.append(-1)
        else:
            out.append(stack[-1])
            stack.pop()
    elif command == "size":
        out.append(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            out.append(1)
        else:
            out.append(0)
    elif command == "top":
        if len(stack) == 0:
            out.append(-1)
        else:
            out.append(stack[-1])
    else:
        stack.append(command.split(" ")[1])

for i in out:
    print(i)