class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class  Employee(Person):
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company

    def get_info(self):
        return f"{self.name}, {self.age} years old, works at {self.company}" 
    
e = Employee("Hasan", 25, "Google")
print(e.get_info())    


