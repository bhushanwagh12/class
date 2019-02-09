# write a program to create a student class and create a object to it
# and call the method talk to display the student data.

class Student:
    def __init__(self,id,name,roll,course,college,fees):
        self.id=id
        self.name=name
        self.roll=roll      # declaring instance variable
        self.course=course
        self.college=college
        self.fees=fees
    def talk(self):
        print("student ID :",self.id)
        print("student name :",self.name)   # initializing the instance variable.
        print("student roll :",self.roll)
        print("student course :",self.course)
        print("student college :",self.college)
        print("student fees :",self.fees)
s=Student(101,"bhushan",23,"MCA","K K Wagh college",25500)  # creating an object.
s.talk()
