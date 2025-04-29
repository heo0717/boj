N = int(input()) #number 0 ~ n-1
P = list(map(int, input().split())) #money for num
M = int(input()) #money i own

#biggest room number
#the longer the digits, the greater the num

if len(set(P)) == 1 :
    digit_count = M // P[0]

    if digit_count == 0 :
        print(0)
    else :
        room_num = [N - 1] * digit_count
        print(int(''.join(map(str,room_num))))

else :
    room_num = []

    min_price = min(P)
    min_num = P.index(min_price)

    #but the first digit can't be zero
    if min_num == 0 :
        sec_min_price = float('inf')
        sec_min_num = -1 #invalid index 
        for i in range(1, N):
            if P[i] < sec_min_price :
                sec_min_price = P[i] 
                sec_min_num = i       

        if sec_min_num == -1:
            print(0)
            exit()
        
        if M < sec_min_price :
            print(0)
            exit()

        M -= sec_min_price
        digit_count = 1 + (M // min_price)
        M -= (digit_count - 1) * min_price

        room_num = [sec_min_num] + [min_num] * (digit_count - 1)

    else :
        digit_count = M // min_price
        if digit_count == 0:
            print(0)
            exit()
        M -= digit_count * min_price
        room_num = [min_num] * digit_count

    for i in range(digit_count):
            for num in range(N - 1, -1, -1):
                # M = M + current_prince - P[num]
                current_digit = room_num[i]
                current_price = P[current_digit]
                 
                if M + current_price >= P[num] and num > current_digit :
                    M = M + current_price - P[num]
                    room_num[i] = num
                    break
    
    print(''.join(map(str,room_num)))

#--------------------------------------------------------

# i = N-1
# room_num = []
# while True :

#     if M < P[0] :
#         print(int(''.join(map(str,room_num))))
#         break
    
#     if M >= P[i] :
#         room_num.append(i)
#         M -= P[i]

#     else :
#         i -= 1