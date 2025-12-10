import sys
input = sys.stdin.readline

vowels = set("aeiou")

while True:
    raw = input()
    if not raw:  # EOF 방어
        break
    s = raw.strip()  # 줄바꿈 제거

    if s == "end":
        break

    # 1) 모음이 하나 이상 포함
    if not any(ch in vowels for ch in s):
        print(f"<{s}> is not acceptable.")
        continue

    # 2) 모음/자음이 3개 이상 연속 금지
    v_run = c_run = 0
    bad = False
    for ch in s:
        if ch in vowels:
            v_run += 1
            c_run = 0
        else:
            c_run += 1
            v_run = 0
        if v_run >= 3 or c_run >= 3:
            print(f"<{s}> is not acceptable.")
            bad = True
            break
    if bad:
        continue

    # 3) 같은 글자 연속 금지 (예외: "ee", "oo")
    ok = True
    for i in range(len(s) - 1):
        if s[i] == s[i+1] and s[i:i+2] not in ("ee", "oo"):
            print(f"<{s}> is not acceptable.")
            ok = False
            break
    if not ok:
        continue

    print(f"<{s}> is acceptable.")
