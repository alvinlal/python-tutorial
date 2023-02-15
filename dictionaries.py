student = {
    "name": "alvin",
    "age": 22,
    "hobbies": [1, 2, 3],
    1: 'john'
}

print(student)
print(student["name"])
print(student.get('test'))  # None
print(student.get('test', 'Not found'))  # Not found
# print(student['test'])  # error
student.update({"name": "jane"})
student.pop('name')
print(student)
print(len(student))  # 3
print(student.values())
print(student.keys())


for key, value in student.items():
    print(key, value)
