# Constructors in Python
class A:
    address = "Lahore"
    def __init__(self):
        self.name = "Asad"
        print(self.name ," live in " , self.address,"." )
obj = A()        


# Destructors in Python
class Students:
    def __init__ (self):
        print("Students are in classroom")
    def __del__ (self):
        print("Students are not in classroom")
def main():
    students = Students()  
    del students
if __name__ == "__main__":
    main()  


# First class function
def Divisions(a,b):
    return a/b
Var = Divisions(12,6)
print(int(Var))    


# Metaprogramming with metaclasses
class MyMetaclass(type):
    pass
class A(metaclass = MyMetaclass):
    pass
def main():
    a = A()
    print(f"{type(a)=}")
    print(f"{type(A)=}")
main()


# Class and instance attribute
class Student:
    def __init__(self,nm,m):
        self.name = nm
        self.marks = m
    def display(self):
        print(self.name,self.marks)    
std1 = Student("Asad : ",94)
std2 = Student("Ahmad : ",89)
std3 = Student("Ali : ",91)       
std1.display()
std2.display()
std3.display()



# Reflection
def Reflection(value):
    type_val = type(value)
    value_0 = type_val()
    if value == value_0:
        return value_0
    prev = Reflection(value[1:])
    value_1 = value[0:1] 
    reflected = prev + value_1
    return reflected
val1 = [1,2,3,4]
test1 = Reflection(val1)
print("Original value" , val1)
print("Reflection Value" , test1)



# Garbage collection
num = 4
num = 5
num = 6
print(num)
