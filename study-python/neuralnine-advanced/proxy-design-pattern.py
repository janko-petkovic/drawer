'''
Quite similar to the decorator "design pattern", you are basically wrapping
functionality around thins. Creates additional layer of protection (?)
'''

from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method(self):
        '''Interface method'''


class Person(IPerson):

    def person_method(self):
        print('I am person.')


class ProxyPerson(Person):
    '''Whenever we are creating the proxy, we will be also creating a Person
    instance.
    '''

    def __init__(self):

        '''This is the characteristic line. Proxy is a wrapper of Person, but
        you expose the proxy, not the Person, adding additional layers of
        encapsulation
        '''
        self.person = Person()

    def person_method(self):
        print("I am the proxy functionality!")
        self.person.person_method()


pp = ProxyPerson()
pp.person_method()

