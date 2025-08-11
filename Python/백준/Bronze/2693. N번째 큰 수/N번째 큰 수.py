# 테스트 케이스의 수 T 입력
t = int(input())

# 테스트 케이스에서 3번째로 큰 값을 출력하는 함수 정의
def find_third(arr):
    first, second, third = 0, 0, 0
    for i in arr:
        if i > first:
            third = second
            second = first
            first = i
        elif i > second:
            third = second
            second = i
        elif i > third:
            third = i
    return third

# 반복문을 통해 T번 반복 출력
for i in range(t):
    arr = list(map(int, input().split()))
    print(find_third(arr))