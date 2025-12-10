import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 듣도 못한 사람 집합
dt = {input().rstrip() for _ in range(n)}
# 보도 못한 사람 집합
bo = {input().rstrip() for _ in range(m)}

# 교집합을 정렬
ans = sorted(dt & bo)

print(len(ans))
print("\n".join(ans))
