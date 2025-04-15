#DP 배열 - 계산값을 미리 저장해둔 리스트

t = int(input())

dp = [0] * 101

dp[1], dp[2], dp[3] = 1, 1, 1

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

for i in range(t):
    n = int(input())
    print(dp[n])