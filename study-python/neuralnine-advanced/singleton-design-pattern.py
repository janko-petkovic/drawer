'''
Actually quite simple.
Each class can have ONLY A SINGLE CLASS INSTANCE (called singleton)
'''

from abc import ABCMeta, abstractmethod
from typing import Type, Self

class IPerson(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def get_instance() -> "PersonSingleton | None":
        '''Implement in child class'''
        pass


class PersonSingleton(IPerson):
    '''The instance variable is going to point the one instance we have of this
    class. Notice that it makes sense now to use abstract methods I guess.
    '''
    __instance = None

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception('Singletons cannot be istantiated more than once.')
        self.name = name
        self.age = age
        PersonSingleton.__instance = self

    @staticmethod
    def get_instance():
        return PersonSingleton.__instance

    def __repr__(self):
        return( f'PersonSingleton(name={self.name},age={self.age})')



print(PersonSingleton.get_instance())
ps = PersonSingleton('giorgio', 4)
print(PersonSingleton.get_instance())
ps = PersonSingleton('giorgio', 4)





