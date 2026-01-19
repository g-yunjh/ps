def solution(brown, yellow):
    total = brown + yellow
    for w in range(3, total // 3 + 1):
        if total % w == 0:
            h = total // w
            if (w - 2) * (h - 2) == yellow:
                return [max(w,h), min(w, h)]