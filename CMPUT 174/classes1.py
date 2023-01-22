class Student:
    '''any fucntion thatt exist inside a class is called a methd'''
    def __init__(self  ,my_name, my_id):  # initializer
        ''' The first parameter in a methid is always self
        properties are initilized in the __init__method
        2 . properties - instance attributes - all instance attributes are reffered to by the word self'''
        
        self.name = my_name
        self.student_id = my_id

    # Behavior
    def display(self):
        print(self.name,self.student_id)


def main():
    ''' A class is a callable in python, just like you call a functon,
    when you call a class 
    1.   you create an object that is an instance of that class 
    2.   the init method in the class is called implicitly '''
    student1 = Student('fred', 1234)  # Student object has come into existence with 2 properties
    student1.display()
    student2 = Student('Hiritikk', 1782594)
    student2.display()
    student3 = Student('barney', 172515)
    student3.display()

main()
    