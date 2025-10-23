student = {
    "name": "Taqi",
    "age": 13,
    "course": "Python"
}

print(student["name"]) 
print(student.get("age"))
print(student.get("course"))


product = {
    "id": 219,
    "name": "Laptop",
    "price": 499.99,
    "stock": 50
}

product["price"] = 319.99
print(product)

product.pop("stock")
print(product)

product.clear()
print(product)

for key in student:
    print(key, ":", student.get(key))

students = {
    "s1": {"name": "Ali", "age": 20},
    "s2": {"name": "Arham", "age": 21}
}

print(students["s1"]["name"])