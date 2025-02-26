import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
tanghuru = input().split() 

count_fruits = defaultdict(int)

left = 0
tanghuru_length = 0
for right in range(N) :
    count_fruits[tanghuru[right]] += 1

    while len(count_fruits) > 2:
        count_fruits[tanghuru[left]] -= 1
        if count_fruits[tanghuru[left]] == 0:
            del count_fruits[tanghuru[left]]
        left += 1
    
    tanghuru_length = max(tanghuru_length , right - left + 1)

print(tanghuru_length)