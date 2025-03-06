S = input().strip()
s = list(S)

a = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        a.append(''.join(s[i:j]))

result = set(a)
print(len(result))