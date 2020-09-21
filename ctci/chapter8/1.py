# 8.1: Triple Step

def countWays(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp)
    return dp[n]

print(countWays(3))
print(countWays(4))
print(countWays(5))
print(countWays(6))

