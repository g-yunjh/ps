words = [list(input()) for _ in range(5)]

max_len = max(len(word) for word in words)

for word in words:
    if len(word) < max_len:
        word += [''] * (max_len - len(word))

for i in range(max_len):
    for j in range(5):
        print(words[j][i], end = '')