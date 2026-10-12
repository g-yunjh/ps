from collections import defaultdict

def solution(message, spoiler_ranges):
    # 1. 스포일러 인덱스 마킹
    sp = [False] * len(message)
    for s in spoiler_ranges:
        for i in range(s[0], s[1] + 1):
            sp[i] = True

    total_count = defaultdict(int)    # 단어별 전체 등장 횟수
    spoiler_count = defaultdict(int)  # 단어별 스포일러 등장 횟수

    # 2. 공백 기준으로 단어 분리 및 인덱스 추적
    n = len(message)
    i = 0
    while i < n:
        if message[i] == ' ':
            i += 1
            continue
        
        start = i
        while i < n and message[i] != ' ':
            i += 1
        end = i  # 단어가 끝나는 인덱스 (exclusive)

        word = message[start:end]
        
        # 해당 단어 영역 내에 스포일러(True)가 하나라도 포함되어 있는지 확인
        is_spoilered = any(sp[j] for j in range(start, end))

        total_count[word] += 1
        if is_spoilered:
            spoiler_count[word] += 1

    # 3. 모든 등장 위치에서 스포일러 처리된 단어("중요한 단어") 개수 카운트
    cnt = 0
    for word, count in total_count.items():
        if spoiler_count[word] == count:
            cnt += 1

    return cnt