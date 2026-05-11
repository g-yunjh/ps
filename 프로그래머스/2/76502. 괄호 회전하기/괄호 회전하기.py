def solution(s):
    cnt = 0
    for i in range(len(s)):
        t = s[i:] + s[:i]
        arr = []
        for j in t:
            if j in ["[", "{", "("]:
                arr.append(j)
            else:
                if arr != []:
                    if j == "]" and arr[-1] == "[":
                        arr.pop()
                    elif j == "}" and arr[-1] == "{":
                        arr.pop()
                    elif j == ")" and arr[-1] == "(":
                        arr.pop()
                    else:
                        break
        if t[0] in ["[", "{", "("] and arr == []:
            cnt += 1
    return cnt