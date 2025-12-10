import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    else:
        arr.append(word)
    
word_counts = {}

for i in arr:
    word_counts[i] = word_counts.get(i, 0) + 1

# sort
sorted_arr = sorted(word_counts.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# output
for word, count in sorted_arr:
    print(word)
 