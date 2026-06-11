def solution(phone_book):
    # 1. 모든 전화번호를 해시 맵(딕셔너리)에 등록
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    # 2. 각 번호의 접두어가 해시 맵에 존재하는지 확인
    for phone_number in phone_book:
        jumsu = ""
        for number in phone_number:
            jumsu += number
            if jumsu in hash_map and jumsu != phone_number:
                return False
                
    return True