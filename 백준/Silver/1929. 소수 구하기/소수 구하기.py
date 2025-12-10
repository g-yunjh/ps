import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# True=소수라고 가정하고 시작
is_prime = bytearray(b"\x01") * (n + 1)
if n >= 0: is_prime[0] = 0
if n >= 1: is_prime[1] = 0

# i*i부터 지우기
limit = int(n**0.5)
for i in range(2, limit + 1):
    if is_prime[i]:
        step = i
        start = i * i
        is_prime[start:n+1:step] = b"\x00" * (((n - start) // step) + 1)

out = []
start = m if m >= 2 else 2
for i in range(start, n + 1):
    if is_prime[i]:
        out.append(str(i))

sys.stdout.write("\n".join(out))
