from collections import Counter
from itertools import chain

answer = [list(input().upper().strip()) for _ in range(3)]
guess = [list(input().upper().strip()) for _ in range(3)]

answer_counts = Counter(chain.from_iterable(answer))

green = 0
yellow = 0
for i in range(3):
    for j in range(3):
        if answer[i][j] == guess[i][j]:
            green += 1
            answer_counts[answer[i][j]] -= 1

for i in range(3):
    for j in range(3):
        if ( answer[i][j] != guess[i][j] ) and answer_counts.get(guess[i][j],0)>0 :
            yellow += 1
            answer_counts[guess[i][j]] -= 1
        
print(green)
print(yellow)