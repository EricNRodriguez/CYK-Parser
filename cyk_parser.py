from grammar import Grammar
from invalid_symbol_error import InvalidSymbolError
from production_rule import ProductionRule

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
            for production_rule in self.get_grammar().get_production_rules():
                for body in production_rule.get_bodys():
                    if len(body) == 1 and body[0] == char:
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


    def parse_grammar(self, filepath):
        """
        Parses grammar from EBNF form to a Grammar object
        :param filepath:
        :return Grammar object:
        """

        # assert that its actually a filepath !!!

        # g = Grammar()

        production_rules = {}
        bodys = {}

        with open(filepath) as file:
            for line in file:
                if line != "\n":
                    line = line.replace(" ", "").replace(";", "").strip("\n").split("=")
                    var_bodys = line[1].replace(";", "").split("|")
                    if line[0] != "":
                        production_rules[line[0]] = ProductionRule(line[0])
                        bodys[line[0]] = [*bodys.get(line[0], []), *var_bodys]


        # build bodys
        for variable in bodys:
            print("----")
            for body in bodys[variable]:
                body = body.split(",")
                for pr in production_rules:
                    for i, b in enumerate(body):
                        if b == pr:
                            body[i] = production_rules[pr]
                    production_rules[pr].add_bodys(body)



                # convert




        for k in production_rules:
            print(production_rules[k].get_variable())
            print(production_rules[k].get_bodys())
            print(len(production_rules[k].get_bodys()))
            print("--")
        return
