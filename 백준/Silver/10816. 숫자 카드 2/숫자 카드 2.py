def count_by_range(array, target):
    n = len(array)
    
    # 1. 가장 왼쪽 인덱스 찾기 (Lower Bound)
    def get_left_index():
        start, end = 0, n - 1
        res = -1
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                res = mid
                end = mid - 1  # 찾았어도 더 왼쪽을 확인
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return res

    # 2. 가장 오른쪽 인덱스 찾기 (Upper Bound)
    def get_right_index():
        start, end = 0, n - 1
        res = -1
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                res = mid
                start = mid + 1 # 찾았어도 더 오른쪽을 확인
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return res

    left = get_left_index()
    if left == -1: # 애초에 데이터가 없으면 0 반환
        return 0
    
    right = get_right_index()
    return right - left + 1

# 입력부
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
x = list(map(int, input().split()))

# 결과 출력
for i in x:
    print(count_by_range(arr, i), end=" ")
