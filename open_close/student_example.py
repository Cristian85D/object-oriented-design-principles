import random

from abc import ABC, abstractmethod


class DiscountCalculator:
    """
    We did not have to change any other class to handle discount percentage.
    Adding to the software component, should not have to modify existing code.
    Adding a new type of Student, not modify the code of calculate_discount_percentage
    """

    @staticmethod
    def calculate_discount_percentage(student):
        if student.has_discount():
            return 20
        return 0


"""
We get robust designs that are easy to extend in future
"""

class StudentProfile(ABC):
    """
    common interface class
    """

    @abstractmethod
    def has_discount(self):
        pass


class UniversityStudent(StudentProfile):
    def has_discount(self):
        return random.choice([True, False])


class HighSchoolStudent(StudentProfile):
    def has_discount(self):
        return random.choice([True, False])


class ElementarySchoolStudent(StudentProfile):
    """
    A software component(class, module, method) should be extendable to add a
    new feature or to add a new behavior to it.
    This is the new feature: ElementarySchoolStudent that implement the
    StudentProfile interface
    """
    def has_discount(self):
        return random.choice([True, False])


if __name__ == '__main__':
    print(f'UniversityStudent percentage discount: '
          f'{DiscountCalculator.calculate_discount_percentage(UniversityStudent())}'
          f'')
    print(f'HighSchoolStudent percentage discount: '
          f'{DiscountCalculator.calculate_discount_percentage(HighSchoolStudent())}'
          f'')
    print(f'ElementarySchoolStudent percentage discount: '
          f'{DiscountCalculator.calculate_discount_percentage(ElementarySchoolStudent())}'
          f'')
