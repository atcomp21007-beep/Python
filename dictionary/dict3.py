students = {
    "101": {"name": "Taqi", "marks": 99},
    "102": {"name": "Arham", "marks": 61},
    "103": {"name": "Mustafa", "marks": 71}
}

roll = input("Enter roll number:")

if roll in students:
    print("Name:", students[roll]["name"])
    print("Marks:", students[roll]["marks"])
else:
    print("STUDENT NOT FOUND!")