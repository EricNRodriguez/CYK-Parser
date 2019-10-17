from production_rule import ProductionRule

class CYKParser():

    def __init__(self, filepath):
        self._grammar = self.__parse_grammar(filepath)

    def parse(self, string):
        assert type(string) is str, "invalid string passed to parse, not of type string"

        parse_table = self.__generate_parse_table(string)

        self.__print_parse_table(parse_table, string)

    def __generate_parse_table(self, string):

        # upper left triangular
        parse_table = [[{} for s in range(len(string) - l)] for l in range(len(string))]

        for i, char in enumerate(string):
            for production_rule in self._grammar:
                if len(production_rule[1]) == 1 and production_rule[1][0] == char:
                    parse_table[0][i][production_rule[0]] = True

        for l in range(2, len(string)+1):
            # length of substring
            for s in range(0, len(string)-l+1):
                # starting index of substring
                for p in range(0, l-1):
                    for production_rule in self._grammar:
                        if len(production_rule[1]) == 2:
                            b = parse_table[p][s].get(production_rule[1][0], False)
                            c = parse_table[l - p - 2][s + p + 1].get(production_rule[1][1], False)
                            if b and c:
                                parse_table[l - 1][s][production_rule[0]] = True

        return parse_table

    def __print_parse_table(self, table, string):

        table = table[::-1]
        for i in range(0, len(table)):
            for j in range(0, len(table[i])):
                print('{} | '.format((repr([k for k in table[i][j].keys()])).center(40)), end = " ")

            print('\n', '=' * 43 * len(table[i])) if i == len(table) - 1 else print('\n', '-' * 43 * len(table[i]))

        for char in string:
            print('{}|| '.format(char.center(40)), end = " ")
        return


    def __parse_grammar(self, filepath):
        """
        Parses grammar from EBNF form to a Grammar object
        :param filepath:
        :return Grammar object:
        """
        production_rules = []
        with open(filepath) as file:

            for line in file:
                line = line.replace(" ", "").replace(";", "").replace("\n", "").split("=")

                if len(line) == 2:
                    production_rules.extend([(line[0], body.split(",")) for body in line[1].split("|")])

        # create instances
        production_rule_objects = {}


        print(production_rules)
        return production_rules