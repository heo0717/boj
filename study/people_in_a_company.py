n = int(input().strip())

people = {}

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        people[name] = True
    elif status == 'leave':
        people.pop(name, None)

for name in sorted(people.keys(), reverse = True):
    print(name)