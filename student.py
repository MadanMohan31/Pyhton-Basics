'''
class is used to define the particular instance of an object.
in this code we build the student class and define the variables in which the values will be stired and executed.
class can be used anytime in other codes by using import function.
'''

class student:
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
