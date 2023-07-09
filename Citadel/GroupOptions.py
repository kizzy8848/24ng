def main(n: int, k: int):
    if k > n:
        return 0

    dp = [[0 for i in range(n + 1)] for j in range(k + 1)]
    print(dp)
    for i in range(1, k + 1):
        for j in range(i, n + 1):
            print(i, j)
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - i]
    return dp[k][n]


if __name__ == "__main__":
    print(main(8,4))

