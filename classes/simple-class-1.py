class Employee:
    name = "Beacon"  # global/shared variables

    def __init__(self, employee_name):
        self.name = employee_name  # instance variables, variable hiding
        self.dept = "some dept"


print(Employee.name)
e = Employee("Fire")
print(e.name)
print(e.dept)

