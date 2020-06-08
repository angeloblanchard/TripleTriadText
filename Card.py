class Card:
    def __init__(self, name, category, values):
        self.name = name
        self.category = category
        self.values = values
        self.top_val = self.values[0]
        self.left_val = self.values[1]
        self.right_val = self.values[2]
        self.bot_val = self.values[3]