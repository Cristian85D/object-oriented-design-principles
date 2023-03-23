"""
Student class is tightly coupled with the database layer because the Student
class made cognizant of the low level details related to dealing with database
layer and calculate tax layer.
Tight coupling is an undesirable feature in software.
"""

class Employee:
    """
    Responsibilities:
        1. handle core employee profile data.
        2. dealing with database operations. -> The Student class should NOT be made cognizant of the low level details related to dealing with database layer.
        3. dealing with calculate tax -> The Student class should NOT be made cognizant of the low level details related to calculate tax.

    Reasons to change:
        1. A change in the employee id format.
        2. A change in the employee name format.
        3. A change in the database layer.
        4. A change in the calculate tax.
    """

    def __init__(self, id, name, address, type):
        self.id = id
        self.name = name
        self.address = address
        self.type = type

    def save(self):
        """
        Student class is tightly coupled with the database layer because the
        Student class made cognizant of the low level details related to
        with database layer.
        """
        print(f'Saving employee: {self.__dict__} in database')

    def calculate_tax(self):
        """
        Student class is tightly coupled with the calculate tax because the
        Student class made cognizant of the low level details related to
        with calculate tax.
        """
        print(f'Tax calc for employee: {self.__dict__}')
        if self.type == 'full_time':
            print('Tax calc for full time employee')

        if self.type == 'contract':
            print('Tax calc for contractors')


if __name__ == '__main__':
    st = Employee(31890233, 'Cristian', 'Lagos 4567', 'full_time')
    st.save()
    st.calculate_tax()
