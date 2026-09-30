def solution(record):
    d = {}
    for i in record:
        if i.split()[0] in ["Enter", "Change"]:
            d[i.split()[1]] = i.split()[2]
    
    result = []
    for i in record:
        if i.split()[0] == "Enter":
            result.append(f"{d[i.split()[1]]}님이 들어왔습니다.")
        elif i.split()[0] == "Leave":
            result.append(f"{d[i.split()[1]]}님이 나갔습니다.")
    return result