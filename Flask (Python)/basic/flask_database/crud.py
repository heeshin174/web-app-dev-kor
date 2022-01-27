# Perform basic CRUD on our model (CRUD stands for create, read, update, delete)
# import the database
from main import db, Student

# add a new record
new_student = Student('John', 80)
db.session.add(new_student)
db.session.commit()

# Reading all students or a specific student using the id
all_students = Student.query.all() # List all all_students
print(all_students) # [Student Mahmut got 100 on midterm exam, Student Sam got 105 on midterm exam, Student John got 90 on midterm exam

# Select the student by id
first_student = Student.query.get(1)
print(first_student.name) # Mahmut

# Display students whose grade is bigger than 85
# Filter
student_pass = Student.query.filter(Student.grade>=85)
print(student_pass.all()) # [Student Mahmut got 100 on midterm exam, Student Sam got 105 on midterm exam]

# Update an entry or delete an entry
# update
first_student = Student.query.get(1)
first_student.grade = 105
db.session.add(first_student)
db.session.commit()

# delete
second_student = Student.query.get(2)
db.session.delete(second_student)
db.session.commit()

all_students = Student.query.all()
print(all_students) # [Student Mahmut got 105 on midterm exam, Student John got 80 on midterm exam]