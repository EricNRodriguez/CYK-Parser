class Grammar():
    def __init__(self, production_rules, terminals, start):
        self._start = start
        self._production_rules = production_rules
        self._terminals = terminals

    def get_production_rules(self):
        return self._production_rules

    def get_terminals(self):
        return self._terminals

    def get_start(self):
        return self._start
