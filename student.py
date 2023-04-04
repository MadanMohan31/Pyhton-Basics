'''
class is used to define the particular instance of an object.
in this code we build the student class and define the variables in which the values will be stired and executed.
class can be used anytime in other codes by using import function.
'''


# here we create only one function inside the class.
class student:
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
    
# here we create two or more class in the same class.
class member:
    
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
        
    def good_student(self):
        if self.gpa >= 7.5:
            return True
        else:
            return False
