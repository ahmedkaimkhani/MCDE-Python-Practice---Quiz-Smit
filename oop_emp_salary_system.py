from abc import ABC, abstractmethod


# Abstract Class
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def employee_details(self):
        pass


# Full-Time Employee
class FullTimeEmployee(Employee):

    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def employee_details(self):
        return "Full-Time Employee: " + self.name


# Part-Time Employee
class PartTimeEmployee(Employee):

    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

    def employee_details(self):
        return "Part-Time Employee: " + self.name


# Contract Employee
class ContractEmployee(Employee):

    def __init__(self, name, contract_amount):
        self.name = name
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount

    def employee_details(self):
        return "Contract Employee: " + self.name


# Creating objects
full_time = FullTimeEmployee("Ali", 80000)
part_time = PartTimeEmployee("Ahmed", 100, 500)
contract = ContractEmployee("Usama", 60000)


# Output
print(full_time.employee_details())
print("Salary:", full_time.calculate_salary())

print(part_time.employee_details())
print("Salary:", part_time.calculate_salary())

print(contract.employee_details())
print("Salary:", contract.calculate_salary())