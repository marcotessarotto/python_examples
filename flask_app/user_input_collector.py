

class UserInputCollector:
    def __init__(self):
        self.total_characters = 0
        self.count = 0

    def add_input(self, user_input):
        self.total_characters += len(user_input)
        self.count += 1

    def is_complete(self):
        return self.count >= 10

    def get_total_characters(self):
        return self.total_characters


