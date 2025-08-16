# 5 people

grade = []
for _ in range(5):
    g = int(input())
    if g < 40 : g = int(40)
    grade.append(g)

print(sum(grade)//5)