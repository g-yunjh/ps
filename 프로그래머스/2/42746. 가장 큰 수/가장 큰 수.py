def solution(numbers):
    arr = []
    for number in numbers:
        arr.append(str(number))
    arr.sort(key = lambda x: x*3, reverse = True)
    
    return str(int("".join(arr)))