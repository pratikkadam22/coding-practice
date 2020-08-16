import itertools, random

class cards:
    """
    This is the base class used to generate the deck, does the in-shuffle and also to get the answer to questions.
    """
    def __init__(self):
        self.deck = []

    def generate_deck(self):
        """
        This method generate the deck of 52 cards.
        """
        self.deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
        random.shuffle(self.deck)

    def inShuffle(self):
        """
        This method does the 'in-shuffle', perfect shuffle on the deck of cards.
        """
        n = len(self.deck) // 2
        res = []
        for i in range(n):
            res.append(self.deck[n + i])
            res.append(self.deck[i])
        self.deck = res
    
    def question1(self):
        """
        This method returns the position of the first card after the 7th shuffle.
        """
        first_card = self.deck[0]
        for i in range(7):
            self.inShuffle()
        return self.deck.index(first_card) + 1
    
    def question2(self):
        """
        This method return the number of times one must perform the shuffle so that the top card
        becomes the bottom card.
        """
        top_card = self.deck[0]
        count = 0
        while top_card != self.deck[len(self.deck)-1]:
            self.inShuffle()
            count += 1
        return count
    
    def question3(self):
        """
        This method returns the number of shuffles after which the first card and the last card touch.
        """
        first_card, last_card = self.deck[0], self.deck[len(self.deck) - 1]
        count = 0
        while True:
            self.inShuffle()
            count += 1
            if self.deck.index(first_card) == self.deck.index(last_card) + 1:
                break
            elif (self.deck.index(first_card) == self.deck.index(last_card) - 1):
                break
        return count

cards = cards()
cards.generate_deck()
print(cards.question1())
print(cards.question2())
print(cards.question3())