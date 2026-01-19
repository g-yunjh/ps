def solution(sizes):
    ga = 0
    se = 0
    for size in sizes:
        size.sort()
        if ga < size[0]:
            ga = size[0]
        if se < size[1]:
            se = size[1]
        
    return ga * se