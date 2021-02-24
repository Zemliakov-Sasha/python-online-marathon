class Employee():
    def __init__(self, firstname, secondname, salary):
        self.firstname = firstname
        self.secondname = secondname
        self.salary = salary

    @classmethod
    def from_string(cls, str):
        str = str.split("-")
        cls.firstname = str[0]
        cls.secondname = str[1]
        cls.salary = str[2]
        return Employee


emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

print(emp1.firstname)
print(emp1.salary)
print(emp2.firstname)
