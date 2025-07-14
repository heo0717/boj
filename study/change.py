money = int(input())

M = 1000 - money

ans = 0 
if M >= 500 :
    ans += M // 500
    M %= 500

if M < 500 and M >= 100 :
    
    ans += M // 100
    M %= 100

if M < 100 and M >= 50 :
    
    ans += M // 50
    M %= 50

if M < 50 and M >= 10 :
    
    ans += M // 10
    M %= 10

if M < 10 and M >= 5 :
    
    ans += M // 5
    M %= 5

if M < 5 :
    ans += M // 1

print(ans)