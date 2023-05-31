class Student:
    def __init__(self, name, id, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa
    
    def show_info(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("GPA:", self.gpa)

class Classroom:
    def __init__(self):
        self.students = []
    
    def add(self, s):
        self.students.append(s)
        print(f'Student {s.name} has been added to the classroom.')
    
    def remove(self, id):
        for s in self.students:
            if s.id == id:
                self.students.remove(s)
                print(f'Student {s.name} has been removed from the classroom.')
    
    def find_best(self):
        if self.students.length == 0:
            print('No student in the classroom.')
            return None
        
        best = self.students[0]
        for s in self.students:
            if s.gpa > best.gpa:
                best = s
        return best
    
    def find(self, name):
        found_students = []
        for s in self.students:
            if s.name == name:
                print(f'Found student {s.name} in the classroom.')
                found_students.append(s)
                
        return found_students