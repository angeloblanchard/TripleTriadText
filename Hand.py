class Hand:
    def __init__(self):
        self.cards = []

    def draw_cards(self, card_list):
        print("You draw 5 cards.\nYou draw:")
        for i in range(5):
            card = card_list.draw_card()
            print(card.name, ": Top", card.top_val, "Left", card.left_val, "Right", card.right_val,"Bottom", card.bot_val)
            self.cards.append(card)

    def inspect_hand(self):
        print("\nYou inspect your hand:")
        for i in self.cards:
            print(i.name, ": Top", i.top_val, "Left", i.left_val, "Right", i.right_val,"Bottom", i.bot_val)

