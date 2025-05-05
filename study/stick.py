x = int(input())

# 64cm stick -> X cm stick
# 64 -> 32 -> 16 -> ,, -> 2 -> 1 | 2^n
# 이진수란 어떤 수를 2의 거듭제곱들의 합으로 표현하는 방식dk

print(bin(x).count('1'))