# Initially we will import our db, and Student class from main.py file
from main import db, Student

#Create all the tables
db.create_all()

mahmut = Student('Mahmut', 100)
sam = Student("Sam", 105)

# initially they will print none
print(sam.id) # None

print(mahmut.id) # None

db.session.add_all([mahmut,sam])

db.session.commit()

print(mahmut.id) # 1
print(sam.id)    # 2