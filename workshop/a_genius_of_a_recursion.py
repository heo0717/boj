check_time = 0
def recursion(s, l, r):
    
    global check_time

    if l >= r:
        check_time += 1
        return 1
    elif s[l] != s[r]:
        check_time += 1
        return 0
    else:
        check_time += 1
        return recursion(s, l + 1, r - 1)

def is_palindrome(s):
    return recursion(s, 0, len(s) - 1)

t = int(input())

for i in range(t):
    check_time = 0 #전역변수 초기화
    
    char = input().strip()

    print(is_palindrome(char), check_time)