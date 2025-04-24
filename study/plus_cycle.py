n = int(input())
num = str(n).zfill(2)

new = int(num)
cnt = 0

while True :

    f = int(str(new).zfill(2)[0])
    s = int(str(new).zfill(2)[1])
    result = f + s

    new = s * 10 + (result % 10)

    cnt += 1

    if new == n :
        break

print(cnt)