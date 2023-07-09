from student import Student, Classroom

minh = Student('Minh', 100, 3.5)
minh.show_info()

hoang = Student('Hoang', 101, 3.0)
hoang.show_info()

# Create a classroom
co1101 = Classroom()
co1101.add(minh)
co1101.add(hoang)
co1101.add(Student('Huy', 102, 3.2))
co1101.add(Student('Mai', 103, 3.4))

# Find the best student
best = co1101.find_best()
if best != None:
    best.show_info()

# Find a student
name = input('Enter student name: ')
found_students = co1101.find(name)
for s in found_students:
    s.show_info()