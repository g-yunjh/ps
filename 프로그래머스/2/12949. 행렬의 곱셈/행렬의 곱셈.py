def solution(arr1, arr2):
    # 1. 결과 행렬의 크기 설정: (arr1의 행 수) x (arr2의 열 수)
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    
    # 0으로 채워진 결과 행렬 생성
    ans = [[0 for _ in range(c2)] for _ in range(r1)]
    
    # 3중 반복문
    for i in range(r1):          # 결과 행렬의 행
        for j in range(c2):      # 결과 행렬의 열
            for k in range(c1):  # 행과 열을 곱해 더하는 징검다리 역할
                ans[i][j] += arr1[i][k] * arr2[k][j]
                
    return ans