import sys
input = sys.stdin.readline

def can_place(W, H, S1, S2):
    #horizontal
    if S1[0] + S2[0] <= W and max(S1[1], S2[1]) <= H :
        return True
    if S1[1] + S2[1] <= H and max(S1[0], S2[0]) <= W :
        return True
    return False    

h, w = map(int, input().split())
n = int(input())

size = [ tuple(map(int, input().split())) for _ in range(n) ]
# rotated = [(b,a) for (a, b) in sticker_size]
# or [ t[::-1] for t in sticker_size ]

S = 0
for i in range(n):
    for j in range(i+1,n):

        for s1 in [size[i], (size[i][1], size[i][0])]:
            for s2 in [size[j], (size[j][1], size[j][0])]:
                if can_place(w, h, s1, s2):
                    area = s1[0] * s1[1] + s2[0] * s2[1]
                    S = max(S, area)

print(S)