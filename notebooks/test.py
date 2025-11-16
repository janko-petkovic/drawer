
# We want to create a phone address book. Consider how much you understand this
# intention from the code

# Example one

phone_book = []
phone_book.append(('Pino Daniele', 12345))
phone_book.append(('Renato Zero', 34590))
print(phone_book[0])

# Who is phone_book? What does it do? Who is its firs element? What is 12345?
# Only hint is the variable name, which is also wrong in English

# Example 2

from collections import namedtuple

Contact = namedtuple("Contact", ("NameSurname", "number"))

class PhoneBook:

    def __init__(self):
        self.list_of_contacts_ = []

    def add_contact(self, Contact):
        self.list_of_contacts_.append(Contact)

    def get_contact_by_name(self, name):
        for contact in self.list_of_contacts_:
            if contact.NameSurname == name: return contact
        
        # Handle contact is not present in the book
        print(f'{name} is not presentin the book')
        return Contact('Missing',-1)



# this is the part of the code should be now more expressive
phone_book = PhoneBook()
phone_book.add_contact(Contact('Pino Daniele', 12345))
phone_book.add_contact(Contact('Renato Zero', 23456))
print(phone_book.get_contact_by_name('Renato Zero'))

# Notice that casting pino daniele into a contact could have been implicitly
# done in the add_contact method (we pass name and number and he takes care of
# all). Implicit casting is a matter of debate - it is of course quicker when
# writing, but a pain to debug. The Single Responsibility Principle - SRP states
# that one function should only do one thing, and this is a good rule of thumb
# to keep in mind. 
# Also, by imposing the casting on the coder side, we are double checking that
# add_contact receives what it needs to receive, because if the input is
# malformed it will raise concerns at the Contact level - there are of course
# many ways to achieve this, but this can be thought of the most bomb-proof one,
# which ends up really saving a lot of time. 
# Finally: what if you want to add a house address to your contacts? You just
# modify the Contact object, which also handles a very clean and interpretable
# display of its content, so it will say "address" when you print it.
# This is a stupid example, but I hope it gets the idea through.
                     
