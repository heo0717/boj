import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))

low, high = 0, max(trees)
ans = 0

while low <= high :
    h = (low + high) // 2 #h = mid
    total = sum(max(0, tree-h) for tree in trees )

    if total >= m :
        ans = h
        low = h + 1
    else :
        high = h - 1

print(ans)

#---------------------------------------------time over

# higher_tree = 0

# while True :

#     h_t = sum ( 1 for tree in trees if tree > h ) #잘리는 나무의 개수

#     t += higher_tree
#     if t >= m : break

#     higher_tree = h_t
#     h -= 1

# print(h + 1)