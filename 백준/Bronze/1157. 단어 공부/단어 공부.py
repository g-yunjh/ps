s = input().upper()
s_list = list(set(s))
l = []

for i in s_list:
    count = s.count(i)
    l.append(count)

if l.count(max(l))>= 2:
    print("?")
else:
    print(s_list[l.index(max(l))])