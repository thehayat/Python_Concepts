class Employee:
    raise_amount = 1.04

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_email(self):
        return f"{self.name.lower().replace(' ', '.')}@email.com"

    def increase_salary(self):
        self.salary *= self.raise_amount


class Developer:
    pass


dev1 = Developer("dev1", '001', '30000')
dev2 = Developer("dev2", '002', '40000')

print(dev1.get_email())
print(dev2.get_email())
"""
Notes: Here we can see that although we are not passing any arguments to the developer class. But it gets the email,
Reason is that due to Employee class is inherited as base class and method resolution order first looks into Developer 
and then in employee class.
"""


class Developer:
    raise_amount = 1.10

    def __init__(self, name, id, salary, languages):
        super().__init__(name, id, salary)
        # Employee.__init__(self, name, id, salary) # This does not follow DRY convention. Also this would be wrong while using mutltiple inheritance
        self.languages = languages


dev1 = Developer("dev1", '001', '30000', 'python')
dev2 = Developer("dev2", '002', '40000', 'java')

print(dev1.get_email())
print(dev2.languages())
