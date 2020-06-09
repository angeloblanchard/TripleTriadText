from CardList import CardList
from Hand import Hand

if __name__ == '__main__':
    print("Starting Triple Triad Text...")
    card_list = CardList()
    card_list.shuffle()
    card_list.shuffle()

    hand = Hand()
    hand.draw_cards(card_list)
    hand.inspect_hand()


class Board:
    # Board Values
    # 0 1 2
    # 3 4 5
    # 6 7 8
    def __init__(self, positions=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
        self._positions = positions

    def place_card(self, card, position):
        if isinstance(self.positions[position], int):
            self.positions[position] = card
        else:
            return

    @property
    def positions(self):
        return self.positions

    @positions.setter
    def positions(self, positions):
        self._positions = positions


