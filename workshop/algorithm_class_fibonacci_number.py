# check_r = 0
# def fibonacci_recursion(n):
#     global check_r
#     if n == 1 or n == 2 :
#         check_r += 1
#         return 1
#     else :
#         return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
    
check_d = 0
def fibonacci_dp(n):
    global check_d

    f = [0]*(n + 1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        check_d += 1
    return f[n]

n = int(input().strip())

check_d = 0
# check_r = 0

# fibonacci_recursion(n)

print(fibonacci_dp(n), check_d)