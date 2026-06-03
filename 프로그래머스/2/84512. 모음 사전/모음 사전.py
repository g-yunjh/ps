def solution(word):
    # 각 자리수마다 바뀌는 간격
    # 1번 자리: 781, 2번 자리: 156, 3번 자리: 31, 4번 자리: 6, 5번 자리: 1
    diff = [781, 156, 31, 6, 1]
    arr = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    
    ans = 0
    for i in range(len(word)):
        # 현재 알파벳의 인덱스 * 해당 자리의 간격 + 1(자기 자신)
        ans += arr[word[i]] * diff[i] + 1
        
    return ans