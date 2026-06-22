def solution(brown, yellow):
    x = 1
    while True:
        if yellow % x  == 0 and (x+2)*2 + (yellow/x)*2 == brown:
            return yellow/x+2, x+2
        x += 1