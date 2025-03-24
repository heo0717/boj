N = int(input())

name = [ input() for _ in range(N) ]

len_name = len(name[0])

if N == 1 :
    print(*name)
    exit()

ans = []
for i in range(len_name):
    char = [ s[i] for s in name ]

    if all( c == char[0] for c in char ) :
        ans.append(char[0])
    else:
        ans.append('?')

print(''.join(ans))