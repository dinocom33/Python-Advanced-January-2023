number_of_students = int(input())

students_book = {}

for _ in range(number_of_students):
    student, grade = input().split()
    if student not in students_book:
        students_book[student] = students_book.get(student, [])
    students_book[student].append(float(grade))

for students, grades in students_book.items():
    avg_grade = sum(grades) / len(grades)
    all_grades = " ".join(map(lambda x: f'{x:.2f}', grades))
    print(f"{students} -> {all_grades} (avg: {avg_grade:.2f})")
