import sys

w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

def to_linear(dir, d):
    if dir == 1:      # 북
        return d
    elif dir == 4:    # 동
        return w + d
    elif dir == 2:    # 남
        return w + h + (w - d)
    else:             # 서 (dir == 3)
        return w + h + w + (h - d)

shops = []
for _ in range(n):
    dir, d = map(int, sys.stdin.readline().split())
    shops.append(to_linear(dir, d))

g_dir, g_d = map(int, sys.stdin.readline().split())
guard = to_linear(g_dir, g_d)

perim = 2 * (w + h)

ans = 0
for s in shops:
    diff = abs(guard - s)
    ans += min(diff, perim - diff)

print(ans)
