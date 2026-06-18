class Student: 
    def __init__(self,name: str,roll:int,is_enrolled: bool =True):
        self.name = name
        self.roll = roll
        self.__is_enrolled = is_enrolled
    
    @property
    def is_enrolled(self):
        return self.__is_enrolled
    
    def enroll(self):
        if not self.__is_enrolled:
            return f"{self.name} not enrolled"
        else:
            self.__is_enrolled = True
            return f"{self.name} enrolled succesfully"
    
    def dropout(self):
        if  self.__is_enrolled:
            return f"{self.name} already enrolled"
        else:
            self.__is_enrolled = False
            return f"{self.name} not enrolled "
    
    def display(self):
        return f"{self.name} id {self.roll} has {self.__is_enrolled}"
    
class School:
    def __init__(self):
        self.students = []
    
    def add_student(self,student):
        self.students.append(student)
        print(f"{student.name} has been added")
    
    def find_student(self,name):
        for student in self.students:
            if student.name ==name:
                return student
        return None
    
    def show_all(self):
        for student in self.students:
            print(student.display())

# test

school = School()  

s1 = Student("Karim", 233)
s2 = Student("Rahim", 133)
s3 = Student("Ane", 24)

school.add_student(s1)  
school.add_student(s2)
school.add_student(s3)

print("\n--- All Students ---")
school.show_all()  

print("\n--- Find Student ---")
found = school.find_student("Rahim")  
if found:
    print(found.display())
else:
    print("Student not found")

print("\n--- Enroll ---")
print(s1.enroll())
school.show_all()