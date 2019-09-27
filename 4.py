class Student:
    def __init__(self, sid, age, marks):
        self.sid=sid
        self.age=age
        self.marks=marks

    def valid_marks(self):
        if(self.marks > 0 and self.marks < 101):
            return True
        else:
            return False

    def valid_age(self):
        if(self.age > 20):
            return True
        else:
            return False

    def check_qualification(self):
##        x=valid_marks()
##        y=valid_age()

        if(self.marks >= 65 and self.age > 20):
            return True
        else:
            return False

    def setter(self):
        self.sid=int(input("Enter the Student ID : "))
        self.age=int(input("Enter the Student age : "))
        self.marks=int(input("Enter the Student marks : "))

    def getter(self):
        print("The Student Id is : ", self.sid)
        print("The Student age is : ", self.age)
        print("The Student marks is : ", self.marks)

X=Student(0,0,0)
Y=X.setter()
check=X.check_qualification()
if(check == True):
    print("\n Valid marks and age")
    X.getter()
    print("\n You are eligible")
else:
    print("\n Invalid marks or age")
    
