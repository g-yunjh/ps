def solution(s):
    answer = ''
    
    for i in range(len(s)):
        if i == 0:
            answer += s[i].upper()
        else:
            if s[i - 1] == " ":
                answer += s[i].upper()
            else:
                if s[i].isupper():
                    answer += s[i].lower()
                else:
                    answer += s[i]
    
    return answer