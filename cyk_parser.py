from invalid_symbol_error import InvalidSymbolError

class CYKParser():

    def __init__(self, filepath):
        self._grammar = self.__parse_grammar(filepath)

    def parse(self, string):
        """
        Parses string

        :param string: string to be parsed
        :return: Boolean, true if string is recognised by the grammar, false otherwise
        """
        assert type(string) is str, "invalid string passed to parse, not of type string"

        parse_table = self.__generate_parse_table(string)

        self.__print_parse_table(parse_table, string)

        # string is recongised by grammar, print left derivation
        if parse_table[::-1][0][0].get("S", False):
            self.__print_left_derivation(parse_table, [parse_table[len(string) - 1][0]['S']])
            return True
        else:
            return False

    def __generate_parse_table(self, string):
        """
        Generates CYK parse table

        :param string: string to be parsed
        :raises InvalidSymbolError: char in string is not a terminal in the grammar
        :return: parse table
        """

        # upper left triangular
        parse_table = [[{} for s in range(len(string) - l)] for l in range(len(string))]

        for i, char in enumerate(string):
            for production_rule in self._grammar:
                if len(production_rule[1]) == 1 and production_rule[1][0] == char:
                    parse_table[0][i][production_rule[0]] = (1, production_rule, i, 1)

        if any(map(lambda x : len(x) == 0, parse_table[0])):
            raise InvalidSymbolError("ERROR_INVALID_SYMBOL")

        # length of substring
        for l in range(2, len(string)+1):
            # starting position of substring
            for s in range(0, len(string)-l+1):
                # length of left division
                for p in range(0, l-1):
                    for production_rule in self._grammar:
                        if len(production_rule[1]) == 2:
                            b = parse_table[p][s].get(production_rule[1][0], None)
                            c = parse_table[l - p - 2][s + p + 1].get(production_rule[1][1], None)
                            if not b is None and not c is None:
                                parse_table[l - 1][s][production_rule[0]] = (p, production_rule, s, l)
        return parse_table

    def __print_left_derivation(self, table, alpha):
        """
        Relies on the fact that there always exists a left most derivation. Recursively reduces the left most
        production rule in alpha. Base case when no production rules remain, and alpha is printed a final time.
        Left derivation printed is not unique.

        :param table: cyk parse table
        :param alpha: list containing start production rule
        """

        # find first production
        prod = None
        index = -1
        for i, item in enumerate(alpha):
            if isinstance(item, tuple):
                prod = item
                index = i
                break

        if prod is None:
            return alpha

        p = prod[0]
        s = prod[2]
        l = prod[3]

        # prod is R -> terminal, replace with terminal
        if l == 1:
            terminal = prod[1][1][0]
            alpha[index] = terminal
        else:
            # reduce Ra -> Rb, Rc
            left_cell = table[p][s][prod[1][1][0]]
            right_cell = table[l - p - 2][s + p + 1][prod[1][1][1]]
            alpha = alpha[:index] + [left_cell, right_cell] + alpha[index + 1:]

        # print formatted alpha
        for item in alpha:
            print(item[1][0], end=" ") if isinstance(item, tuple) else print(item, end=" ")
        print()

        self.__print_left_derivation(table, alpha)
        return

    def __print_parse_table(self, table, string):
        """
        Prints CYK parse table to standard out. Cells contain Variable/s.

        :param table:
        :param string:
        :return:
        """

        table = table[::-1]
        for i in range(0, len(table)):
            for j in range(0, len(table[i])):
                print('{} | '.format((repr([k for k in table[i][j].keys()])).center(40)), end = " ")

            print('\n', '=' * 43 * len(table[i])) if i == len(table) - 1 else print('\n', '-' * 43 * len(table[i]))

        for char in string:
            print('{}|| '.format(char.center(40)), end = " ")
        print()
        return


    def __parse_grammar(self, filepath):
        """
        Parses grammar from EBNF form

        :param filepath: file in grammar
        :exception FileNotFoundError:
        :return Grammar object:
        """
        production_rules = []
        with open(filepath) as file:

            for line in file:
                line = line.replace(" ", "").replace(";", "").replace("\n", "").split("=")

                if len(line) == 2:
                    production_rules.extend([(line[0], tuple(body.split(","))) for body in line[1].split("|")])

        return production_rules