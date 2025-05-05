# N이 홀수 일때
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys
input = sys.stdin.readline

n = int(input())

nums = list(int(input()) for _ in range(n))

sorted_nums = sorted(nums)
loc_middle = len(nums) // 2

freq = {}
for num in nums :
    freq[num] = freq.get(num,0) + 1

max_freq = max(freq.values())
modes = [k for k,v in freq.items() if v == max_freq]
modes.sort()

#average
print(round(sum(nums) / len(nums)))
#middle
print(sorted_nums[loc_middle])
#mode
if len(modes) == 1:
    print(modes[0])
else:
    print(modes[1])
#range
print(sorted_nums[-1] - sorted_nums[0])
