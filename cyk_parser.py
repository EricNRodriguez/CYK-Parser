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
        parse_table = [[[] for x in range(len(string) - y)] for y in range(len(string))]

        # base cases
        for i, char in enumerate(string):
            parse_table[0][i] = self.get_grammar().query_production_rules_by_body([char])

        # remaining cases
        for i in range(1, len(string)):
            for j, chars in enumerate(self.__substrings(string, i+1)):
                valid_production_rules = []
                for division in self.__splits(chars):
                    # array of tuples (production rule object, index of bodies)
                    left_production_rules = parse_table[len(division[0])-1][j]
                    right_production_rules = parse_table[len(division[1])-1][j+len(division[0])]
                    for combination in self.__cartesian_product(left_production_rules, right_production_rules):
                        for valid_production_tuple in self.get_grammar().query_production_rules_by_body(combination):
                            if valid_production_tuple not in valid_production_rules:
                                valid_production_rules.append(valid_production_tuple)
                parse_table[i][j] = valid_production_rules

        return parse_table

    def __print_parse_table(self, table, string):

        for i, row in enumerate(table[::-1]):
            for j, cell in enumerate(row):
                print('{} | '.format((repr([pr_tuple[0].get_variable() for pr_tuple in cell])).center(40)), end = " ")
            if i == len(table) - 1:
                print('\n', '=' * 43 * len(row))
            else:
                print('\n', '-' * 43 * len(row))

        for char in string:
            print('{}|| '.format(char.center(40)), end=" ")
        print()
        return

    def __splits(self, s):
        if len(s) == 1: return [s]
        return [[s[0:i+1], s[i+1:]] for i in range(0, len(s)-1)]

    def __substrings(self, string, l):
        return [string[i:i+l] for i in range(0, len(string)-l+1)]

    def __cartesian_product(self, A, B):
        return [[a[0],b[0]] for a in A for b in B]

    def __print_leftmost_derivation(self, string, parse_table):
        pass




