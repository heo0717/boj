n = int(input())

wanted_sits = list(map(int, input().split()))
can_sits = set(wanted_sits)

print(len(wanted_sits) - len(can_sits))