from collections import Counter

N = int(input().strip())
num = list(map(int, input().split())) 
M = int(input().strip())
cards = list(map(int, input().split()))

nums = Counter(num)

list =[]
for i in cards:
    list.append(nums.get(i,0))

print(*list)