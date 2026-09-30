from collections import deque

def solution(order):
    arr1 = deque() # queue
    for i in range(len(order)):
        arr1.append(i+1)
    arr2 = [] # stack
    result = []
    
    for i in range(len(order)):
        if len(arr1) > 0 and order[i] >= arr1[0]:
            while True:
                if order[i] == arr1[0]:
                    result.append(order[i])
                    arr1.popleft()
                    break
                else:
                    arr2.append(arr1[0])
                    arr1.popleft()
        elif len(arr2) > 0 and arr2[-1] == order[i]:
            result.append(order[i])
            arr2.pop()
        else:
            break
        
    return len(result)
                
            
            