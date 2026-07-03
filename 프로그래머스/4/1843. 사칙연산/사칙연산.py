def solution(arr):
    nums = []
    ops = []

    for i, x in enumerate(arr):
        if i % 2 == 0:
            nums.append(int(x))
        else:
            ops.append(x)

    n = len(nums)

    max_dp = [[-float("inf")] * n for _ in range(n)]
    min_dp = [[float("inf")] * n for _ in range(n)]

    # 길이가 1인 구간
    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]

    # 구간 길이
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1

            for k in range(left, right):
                if ops[k] == "+":
                    max_value = max_dp[left][k] + max_dp[k + 1][right]
                    min_value = min_dp[left][k] + min_dp[k + 1][right]
                else:
                    max_value = max_dp[left][k] - min_dp[k + 1][right]
                    min_value = min_dp[left][k] - max_dp[k + 1][right]

                max_dp[left][right] = max(max_dp[left][right], max_value)
                min_dp[left][right] = min(min_dp[left][right], min_value)

    return max_dp[0][n - 1]