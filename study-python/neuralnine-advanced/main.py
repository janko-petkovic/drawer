class Person:

    def __init__(self, name, age, sex):

        self.__name = name
        self.__age = age
        self.__sex = sex

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        assert isinstance(name, str)
        self.__name = name

    @staticmethod
    def mymethod():
        print('Static print')

p = Person('pippo', 21, 'm')
p.Name = 'ciao'

p.mymethod()
Person.mymethod()
