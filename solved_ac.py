import sys

def custom_round(num):
    return int(num + 0.5) if num - int(num) >= 0.5 else int(num)

n, *all_op = map(int, sys.stdin.read().split())

if n == 0:
    print(0)
    exit()

cut = custom_round(n * 15 / 100)

all_op.sort()

final_op = all_op[cut:n-cut]

final_op_avg = custom_round(sum(final_op) / len(final_op))

print(final_op_avg)