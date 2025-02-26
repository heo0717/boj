N, K = map(int, input().split())
days = list(map(int, input().split()))

if N == 1:
    print(1 + K)
    exit()

total_cost = 0
i = 0

while i < N:
    
    j = i
    group_cost = (days[i] - days[i] + 1) + K  # = 1 + K

   
    while j + 1 < N:
        
        cost_extend = (days[j+1] - days[i] + 1) + K
       
        cost_separate = group_cost + (1 + K)

        if cost_extend < cost_separate:
            
            j += 1
            group_cost = cost_extend
        else:
           
            break

    total_cost += group_cost
    i = j + 1

print(total_cost)