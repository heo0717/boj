import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

count = 0
pattern = 0

i=0
while i < M-1 :
    if S[i:i+3] == "IOI":
        pattern += 1
        if pattern >= N:
            count += 1
        i+=2

    else :
        pattern = 0
        i+=1
        
print(count)