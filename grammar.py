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

    def query_production_rules_by_body(self, query):
        return [production_rule  for production_rule in self.get_production_rules() for i, body in enumerate(production_rule.get_bodys()) if body == query]


