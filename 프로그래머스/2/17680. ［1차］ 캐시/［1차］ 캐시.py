def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    arr = []
    cnt = 0
    for i in range(len(cities)):
        city  = cities[i].lower()
        if city in arr :
            cnt += 1
            arr.remove(city)
            arr.append(city)                
        elif len(arr) == cacheSize:
            cnt += 5
            arr.remove(arr[0])
            arr.append(city)
        else:
            cnt += 5
            arr.append(city)
            
    return cnt
            
            
            
        