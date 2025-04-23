import sys
input = sys.stdin.readline

n = int(input().strip())
divisors = list(map(int, input().split()))

if len(divisors) == 1:
    print(divisors[0] ** 2)

else :
    sorted_divisor = sorted(divisors)
    print(sorted_divisor[0] * sorted_divisor[-1])