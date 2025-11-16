'''
Apparently very simple.
Multiple classes inherit from a single parent, and "one of those can consist of
many". Wtf smt with subregions.
'''

from abc import ABCMeta, abstractmethod

class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees) -> None:
        pass

    # @staticmethod
    @abstractmethod
    def print_department(self) -> None:
        pass


class Accounting(IDepartment):

    def __init__(self, employees) -> None:
        self.employees = employees

    # @staticmethod
    def print_department(self) -> None:
        print(f'Acconting department: {self.employees}')


class ParentDepartment(IDepartment):

    def __init__(self, employees)

