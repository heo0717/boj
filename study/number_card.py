N = int(input().strip())
s_num = set( map(int, input().split()) )

M = int(input().strip())
num = list(map(int, input().split()))
set_num = set(num)

intersection = s_num & set_num

result = []
for i in num:
    if i in intersection :
        result.append('1')
    else:
        result.append('0')

print(*result)