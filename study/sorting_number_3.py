import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())

counting_sort = [0] * 10001

for _ in range(N) :
    counting_sort[int(input())] += 1

# i = 1이고 cnt[i]=5000000일때, '1\n'은 1 + \n 으로 총 2글자가 되어 문자열길이=2
# 따라서 2 × 5,000,000 = 10MB짜리 문자열이 생겨버리기 때문에 문자열 초과
# 문자열의 곱은 결과 전체길이를 새문자열에 할당하는것
# for i in range(1, len(counting_sort)):
#     if counting_sort[i] :
#         write((str(i) + '\n') * counting_sort[i] )

for i in range(1, len(counting_sort)):
    c = counting_sort[i]
    while c :
        write(f'{i}\n')
        c -= 1