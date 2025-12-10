import sys
sys.setrecursionlimit(1_500_000)
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path halving
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    # union by size (크기가 큰 루트로 합치기)
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

n, m = map(int, input().split())
parent = list(range(n + 1))
size = [1] * (n + 1)

out = []
for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union(a, b)
    else:
        out.append("YES" if find(a) == find(b) else "NO")

print("\n".join(out))
