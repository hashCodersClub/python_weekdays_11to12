# ### OOPS - Object Oriented Programming Paradigm
# ## Objects -> real life data types [behaviour - by defining functions,properties - varibles defined inside class]
# ## class -> blueprint

class Student:
    name = ""
    rollno = ""
    

    def task_submit(self):
        print("Task submitted")

    def introduce(self):
        print(f"My name is {self.name}")


gaurav = Student()
# bhumi = Student()
# kunal = Student()
# kunal_private = Student()

print(dir(gaurav))





