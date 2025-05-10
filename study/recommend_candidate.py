from collections import defaultdict

n = int(input()) #frame of picture
all_r = int(input()) #entire num of recommendation
R = list(map(int, input().split()))

candidate = []
num_of_recommendation = defaultdict(int)

for r in R :
    
    if r not in candidate:

        if len(candidate) >= n:
            
            min_r = min(num_of_recommendation.values())
            min_c = None

            for c in candidate:
                if num_of_recommendation[c] == min_r:
                    min_c = c
                    break

            if min_c : 
                candidate.remove(min_c)
                del num_of_recommendation[min_c]

        candidate.append(r)
        num_of_recommendation[r] += 1

    else : num_of_recommendation[r] += 1

print(*sorted(candidate))