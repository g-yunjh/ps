def solution(s):
    answer = True
    
    # solution
    if s[0] == ')':
        return False
    if s[len(s)-1] == '(':
        return False
    stack = 0
    for i in s:
        if i == "(":
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                return False
    if stack != 0:
        return False

    return True