def solution(phone_book):
    # 1. 모든 전화번호를 Hash Set에 저장 (조회속도 O(1))
    hash_set = set(phone_book)
    
    # 2. 각 전화번호의 접두어가 hash_set에 존재하는지 확인
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            # 자기 자신은 제외하고, 자른 접두어(temp)가 해시에 있다면 접두어 관계임
            if temp in hash_set and temp != phone_number:
                return False
                
    return True