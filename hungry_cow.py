N, T = map(int,input().split()) #T=구해야하는 Day

deliveries = [tuple(map(int, input().split())) for _ in range(N)]

feed = 0 #먹은 건초더미 수
hay = 0 #배달된 건초더미 수
day = 1

for d_i, b_i in deliveries:
    day_passed = d_i - day

    if hay >= day_passed :
        feed += day_passed
        hay -= day_passed

    else:
        feed += hay
        hay = 0 

    hay += b_i
    day = d_i
    
last_days = T - day + 1
feed += min(hay, last_days)

print(feed)