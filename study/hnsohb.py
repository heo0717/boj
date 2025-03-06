N, M = map(int, input().split())

ever_heard = set((input().strip()) for _ in range(N))
ever_seen = set((input().strip()) for _ in range(M))

who_are_u = ever_heard & ever_seen

print(len(who_are_u))
print("\n".join(sorted(who_are_u)))