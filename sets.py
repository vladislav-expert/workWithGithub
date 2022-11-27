users = {"Tom", "Bob", "Alice", "Tom"}

user = "Tom"
if user in users:
    users.remove(user)
print(users)

students_1 = {"Sam", "Tim", "John"}

students_2 = {"Jessie", "Kate", "Jake"}

students3 = students_1.union(students_2)
print(students3)
