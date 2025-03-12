S = input().strip()
K = input().strip()

only_char = "".join([ char for char in S if not char.isdigit() ])

if K in only_char : print('1')
else: print('0')