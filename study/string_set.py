N,M = map(int, input().split())

string = []
for _ in range(N):
    a = input().strip()
    string.append(a)

check_string = []
for _ in range(M):
    b = input().strip()
    check_string.append(b)

result = set(string) & set(check_string)

cnt = 0
for i in check_string:
    if i in result:
        cnt += 1

print(cnt)