import collections 

Card = collections.namedtuple('Card', ('suit, value'))
card = Card('diamonds', 4)
print(card) 

class FrenchDeck:
    values = [str(n) for n in range(2,11)] + list('JQKA')
    suits = "spades diamonds hearts clubs".split()

    def __init__(self):
        self._cards = [Card(value, suit) for value in self.values
                                         for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, idx):
        return self._cards[idx]




if __name__ == '__main__':
    import doctest
    doctest.testmod()
