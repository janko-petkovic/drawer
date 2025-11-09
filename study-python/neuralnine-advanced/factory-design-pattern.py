'''
OOP pattern (increased separation of concerns)
Decide during runtime what instance you want to create

Abstract: person
Concrete: student/teacher

But you also want the concretization to be decided during runtime.
This design pattern is useful only if you use it in big projects, don't fkn put
it in the notebooks my god.

Code gets more difficult to read, so there is definitely tradeoff
'''

from abc import ABCMeta, abstractstaticmethod, abstractmethod

class IPerson(metaclass=ABCMeta):
    '''
    If something is an interface, we call it I-something
    '''

    @abstractmethod
    def person_method(self):
        '''Interface Method. The interface is just the definition of the
        signature, so no implementation, just signature. I don't know if this
        guys is right but whatever.
        '''

class Student(IPerson):
   
    def __init__(self, name):
        self.name = name
        self.role = 'Student'

    def person_method(self):
        print(f'I am {self.role} {self.name}')


class Teacher(IPerson):
   
    def __init__(self, name):
        self.name = name
        self.role = 'Teacher'

    def person_method(self):
        print(f'I am {self.role} {self.name}')


class PersonFactory:
    '''Notice that this class, the factory, does not contain instance methods,
    only a static builder. I have no idea why this would be useful.
    '''

    @staticmethod
    def build_person(person_type, name):
        match person_type:
            case 'student':
                return Student(name)
            case 'teacher':
                return Teacher(name)
            case _:
                raise ValueError('Wrong person_type inserted.')


s = PersonFactory.build_person('student', 'Paolo')
s.person_method()
