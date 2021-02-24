class Employee:
    def __init__(self, str, **kwargs):
        self.str = str
        self.kwargs = kwargs

        print(self.kwargs)
        self.str = self.str.split(' ')
        self.name = self.str[0]
        self.lastname = self.str[1]
        if len(self.kwargs) != 0:
            for key in kwargs:
                if key == "salary":
                    self.salary = kwargs[key]
            for key in kwargs:
                if key == "height":
                    self.height = kwargs[key]
            for key in kwargs:
                if key == "nationality":
                    self.nationality = kwargs[key]
            for key in kwargs:
                if key == "subordinates":
                    self.subordinates = kwargs[key]


john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese',
                subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])

print(peng.subordinates)

print(mary.lastname)# ➞ "Major"
print(richard.salary)
print(richard.height)# ➞ 178
print(giancarlo.nationality) #➞ "Italian"
print(john.name)# ➞ "John"