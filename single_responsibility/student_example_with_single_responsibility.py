"""
Each class has only one responsibility.
High Cohesion: because Employee class is made up of the class EmployeeRepository
and the TaxCalculator class.
Loose coupling: we have removed the tight coupling and made it loose.
"""

class Employee:
    """
    Responsibility: only handle core employee profile data.
    Reasons to change:
        1. A change in the employee id format.
        2. A change in the employee name format.
    """

    def __init__(self, id, name, address, type):
        self.id = id
        self.name = name
        self.address = address
        self.type = type

    def save(self):
        EmployeeRepository.save(self)

    def calculate_tax(self):
        TaxCalculator.calculate_tax(self)


class EmployeeRepository:
    """
    Responsibility: only dealing with database operations.
    Reasons to change:
        1. A change in the database layer.
    We have removed the tight coupling and made it loose.
    So now if we change the underlying database, the Student class does NOT
    need to get changed and recompiled.
    You only need to change the Repository class.
    """

    @staticmethod
    def save(employee:Employee):
        print(f'Saving employee: {employee.__dict__} in database')


class TaxCalculator:
    """
    Responsibility: only dealing with calculate tax.
    We have removed the tight coupling and made it loose.
    So now if we change the underlying calculate_tax, the Student class does NOT
    need to get changed and recompiled.
    You only need to change the TaxCalculator class.
    """

    @staticmethod
    def calculate_tax(employee:Employee):
        print(f'Tax calc for employee: {employee.__dict__}')
        if employee.type == 'full_time':
            print('Tax calc for full time employee')

        if employee.type == 'contract':
            print('Tax calc for contractors')


if __name__ == '__main__':
    st = Employee(31890233, 'Cristian', 'Lagos 4567', 'full_time')
    st.save()
    st.calculate_tax()
