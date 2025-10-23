students = {
    "Ali": int(input("Enter the marks of Ali:")),
    "Taqi": int(input("Enter the marks of Taqi:")),
    "Meera": int(input("Enter the marks of Meera:"))
}
print(students)
print("So,")
top_student = max(students, key=students.get)
print(f"Top Student is {top_student} with the grade of {students[top_student]}")