import sys
input = sys.stdin.readline

T = int(input())

cnt = 0
while True :
    if cnt == T : break

    n = int(input()) #num of applicant
    hired = 0

    grade = [ tuple(map(int, input().split())) for _ in range(n) ]
    grade.sort(key = lambda x : x[0])

    b = float('inf')

    for _, i_rank in grade :
        if i_rank < b :
            hired += 1
            b = i_rank

    print(hired)
    cnt += 1