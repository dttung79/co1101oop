from person04 import Person
from staff04 import Staff
from student04 import Student
from user04 import User


def get_users():
    guest = Person("Alice")
    admin = User("Bobby", "bob01")
    staff1 = Staff("Chris", "chr02", "Lecturer")
    staff2 = Staff("Diana", "dia03", "Professor")
    student1 = Student("Eddie", "edd04", "BSc Computing")
    student2 = Student("Frank", "fra05", "BSc Computer Science")
    student3 = Student("Gerri", "ger06", "MSc Data Science")

    staff1.modules.append("UG1234")
    student1.modules.append("UG1234")
    student1.modules.append("UG2345")
    student1.modules.append("St1234")
    student2.modules.append("UG1234")
    student2.modules.append("UG2345")
    student2.modules.append("St1234")
    staff2.modules.append("UG2345")
    staff2.modules.append("PG1234")
    student3.modules.append("PG1234")
    student3.modules.append("St1234")

    users = [guest, admin, staff1, staff2, student1, student2, student3]
    return users
