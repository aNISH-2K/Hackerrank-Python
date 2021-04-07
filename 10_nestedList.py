'''
# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.
'''
students = []
score_list = []
for _ in range(int(input())):
    temp = []
    name = input()
    score = float(input())
    temp.append(name)
    temp.append(score)
    score_list.append(score)
    students.append(temp)
score_list = list(dict.fromkeys(score_list))
score_list.sort()

if len(students) >= 2:
    second_lowest_students = []
    second_lowest_score = score_list[1]
    for i in students:
        if second_lowest_score in i:
            # print(i[0])
            second_lowest_students.append(i[0])
        else:
            pass
    print('\n'.join(sorted(second_lowest_students, key=lambda second_lowest_students: second_lowest_students)))
else:
    print(students[0][0])
