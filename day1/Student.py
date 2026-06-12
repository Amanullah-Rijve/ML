class Student:
    # constructor parametarised
    def __init__(self,roll_num:int ,math_mark: int,chemistry_mark:int,phy_mark:int):
        self.roll_num = roll_num
        self.math_mark = math_mark
        self.chemistry_mark = chemistry_mark
        self.phy_mark = phy_mark
    # average marks
    def average(self):
        return round((self.math_mark + self.chemistry_mark + self.phy_mark)/3,2)
    # student result
    def result(self):
        if(self.average() >=40):
            return "pass"
        else: return "Fail"
    # display student info
    def display(self):
        return f"student {self.roll_num} average mark is {self.average()} and student {self.result()}"
# creating object for student cals
st1 = Student(2,39,55,60)
st2 = Student(4,50,50,70)
#printing info about student 1 and 2
#student 1
print(st1.display())
#student 2
print(st2.display())