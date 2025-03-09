import sys
input = sys.stdin.readline

ones_melon = int(input())
farm = []
for _ in range(6):
    info = list(map(int, input().split()))
    farm.append(info)

#r가장 긴 변은 서로 이웃함 / 가장 긴 변 + 3 = 가장 작은 변

w, h = 0, 0
for dir, len in farm:
    if dir in [1,2]:
        w = max(w,len)
    else :
        h = max(h,len)

s_w, s_h = 0,0
for i in range(6):
    if (farm[i][1] == w and farm[(i+1)%6][1] == h) or (farm[i][1] == h and farm[(i+1)%6][1] == w) :
        s_w = farm[(i+3)%6][1]
        s_h = farm[(i+4)%6][1]
        break

S = (w*h) - (s_w*s_h)

print(S*ones_melon)