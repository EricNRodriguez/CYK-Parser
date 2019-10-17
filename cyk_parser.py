from grammar import Grammar
from invalid_symbol_error import InvalidSymbolError

class CYKParser():

    def __init__(self, grammar):
        assert type(grammar) is Grammar, "invalid grammar passed to CYKParser, not of type Grammar"
        self._grammar = grammar

    def get_grammar(self):
        return self._grammar

    def set_grammar(self, grammar):
        assert type(grammar) is Grammar, "invalid grammar passed to set_grammar, not of type Grammar"
        self._grammar = grammar

    def parse(self, string):
        assert type(string) is str, "invalid string passed to parse, not of type string"

        if any(s not in self._grammar.get_terminals() for s in string):
            raise InvalidSymbolError("string contains invalid characters")

        parse_table = self.__generate_parse_table(string)

        self.__print_parse_table(parse_table, string)

    def __generate_parse_table(self, string):

        # upper left triangular
        parse_table = [[{} for s in range(len(string) - l)] for l in range(len(string))]

        for i, char in enumerate(string):
            # change query production rules by body to get terminal production rules?
            for production_rule in self.get_grammar().query_production_rules_by_body([char]): #BAD BRO
                parse_table[0][i][production_rule] = True

        for l in range(2, len(string)+1):
            for s in range(0, len(string)-l+1):
                for p in range(0, l-1):
                    for production_rule in self.get_grammar().get_production_rules():
                        for body in production_rule.get_bodys():
                            if len(body) > 1:
                                left_division = parse_table[p][s].get(body[0], False)
                                right_division = parse_table[l-p-2][s+p+1].get(body[1], False)
                                if left_division and right_division:
                                    parse_table[l-1][s][production_rule] = True


        return parse_table

    def __print_parse_table(self, table, string):

        table = table[::-1]
        for i in range(0, len(table)):
            for j in range(0, len(table[i])):
                print('{} | '.format((repr([k.get_variable() for k in table[i][j].keys()])).center(40)), end = " ")

            print('\n', '=' * 43 * len(table[i])) if i == len(table) - 1 else print('\n', '-' * 43 * len(table[i]))

        for char in string:
            print('{}|| '.format(char.center(40)), end = " ")
        return


