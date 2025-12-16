def solution(phone_book):
    # 1. 번호를 사전순으로 정렬
    phone_book.sort()
    
    # 2. 인접한 두 번호만 비교하면 됨
    for i in range(len(phone_book) - 1):
        # 뒤에 오는 번호가 앞의 번호로 시작하는지 확인
        if phone_book[i+1].startswith(phone_book[i]):
            return False
            
    return True