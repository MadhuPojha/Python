from employee_class import Employee

class Company:
    def __init__(self) :
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('------------------')

    def pay_employees(self):
        print('Paying Employee')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount:, ${i.calculate_paycheck():,.2f}')
            print('------------------------------------------')

def main():
    my_company = Company()

    emp1 = Employee('Madhu', 'Ojha', 50000)
    my_company.add_employee(emp1)

    emp2 = Employee('Mishti', 'Mishra', 45000)
    my_company.add_employee(emp2)

    emp3 = Employee('Pari', 'Mishra', 40000)
    my_company.add_employee(emp3)

    my_company.display_employees()

    my_company.pay_employees()

main()