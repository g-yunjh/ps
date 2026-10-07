def solution(msg):
    d = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    
    ans = []
    i = 0
    while i < len(msg):
        cnt = 1
        w = ""
        while i + cnt <= len(msg):
            if msg[i:i+cnt] in d:
                w = msg[i:i+cnt]
                cnt += 1
            else:
                break
        ans.append(d.index(w)+1)
        d.append(msg[i:i+cnt])
        i += cnt - 1
            
    return ans
            
        