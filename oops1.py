class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name :", self.name, ", salary :", self.salary)


emp1 = Employee("firstuser", 550000)
emp2 = Employee("seconduser", 787878)

emp1.displayEmployee()
emp2.displayEmployee()

emp1.displayCount()
