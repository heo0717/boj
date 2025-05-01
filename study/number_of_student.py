import sys
input = sys.stdin.readline

n = int(input()) #number of students

student_number = [input().strip() for _ in range(n)]

len_of_id = []
for k in range(1, len(student_number[0]) + 1):
    id = set()

    for num in student_number :
        id.add(num[-k:])

    if len(id) == n : #check whether it is distinguished or not
        print(k)
        break