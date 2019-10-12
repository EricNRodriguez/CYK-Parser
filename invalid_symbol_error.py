class InvalidSymbolError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return "Error : one or more characters in input string is not a terminal in the grammar"

