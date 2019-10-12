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

        for i, row in enumerate(parse_table):
            print("------------ ", i)
            for char in row:
                print("===")
                for pr in char:
                    print(pr[0].get_variable(), " --> ", pr[1])


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





















        #
        #
        #
        # parse_table = {}
        # #
        # # for y in [[[] for x in range(len("baaba") - y)] for y in range(len("baaba"))]:
        # #     print(y)
        #
        # # base cases
        # for c in string:
        #     if not parse_table.get(c, None):
        #         parse_table[c] = [[], c]
        #     for production_rule in self.get_grammar().get_production_rules():
        #         for j, body in enumerate(production_rule.get_bodys()):
        #             if [c] == body and production_rule.get_variable() not in list(map(lambda x : x.get_variable(), parse_table[c][0])):
        #                 parse_table[c][0].append(production_rule)
        #
        #
        # # organise production rules by right hand side
        # production_rule_map = {}
        # for production_rule in self.get_grammar().get_production_rules():
        #     for body in production_rule.get_bodys():
        #         body_tuple = repr(body)
        #         if not production_rule_map.get(body_tuple, None):
        #             production_rule_map[body_tuple] = [production_rule]
        #         elif production_rule not in production_rule_map[body_tuple]:
        #             production_rule_map[body_tuple].append(production_rule)
        #
        #
        # # remaining cases
        # for i in range(1,2):
        #     for substring in self.__substrings(string, i+1):
        #         # print(substring)
        #         # valid_productions = []
        #         for substring_division in self.__splits(substring):
        #             # print(substring_division)
        #             # cartesian product of production rules for left and right division of substring
        #             # print(parse_table[substring_division[0]], "here")
        #             # print(parse_table)
        #             substring_division_bodies = self.__cartesian_product(parse_table[substring_division[0]][0], parse_table[substring_division[1]][0])
        #             for substring_division_body in substring_division_bodies:
        #                 substring_division_body_tuple = repr(substring_division_body)
        #                 # print(substring_division_body_tuple, "-----------------------------------")
        #                 # print(type(substring_division_body_tuple))
        #                 if production_rule_map.get(substring_division_body_tuple, None):
        #                     for pr in production_rule_map[substring_division_body_tuple]:
        #                         # valid_productions.append(pr)
        #                         # valid_productions.append(ProductionRule(pr.get_variable(), substring_division_body))
        #                         # adding to parse table
        #                         parse_table[substring] = [*parse_table.get(substring, []), [pr, substring_division_body]]
        #
        #
        # for k in parse_table:
        #     print()
        #     print()
        #     print()
        #     print(k, " ==== ", parse_table[k])
        #



                #
                #
                # for pr in valid_productions:
                #     for y in pr.get_bodys():
                #         print(pr.get_variable(), " --> ", end = " ")
                #         for d in y:
                #             if type(d) == str:
                #                 print(d)
                #             else:
                #                 print(d.get_variable(), end = "")
                #         print()





                    #
                    # for substring_division_body in substring_division_bodies:
                    #     if production_rule_map.get(tuple(substring_division_body), None):
                    #         valid_productions[substring_division].append([sub, production_rule])




        #




        #
        #
        # # remaining cases
        # for i in range(1, 2):
        #     # substrings to consider
        #     print()
        #     for substr in self.__substrings(string, i+1):
        #
        #         valid_productions = {}
        #         for split_substrs in self.__splits(substr):
        #
        #             #split_substrs = ['b', 'a'] , substr = ba
        #
        #
        #
        #             bodys = self.__cartesian_product(parse_table[split_substrs[0]][0], parse_table[split_substrs[1]][0])
        #
        #
        #             for b in bodys:
        #                 # find production rules that can produce this
        #                 for pr in self.get_grammar().get_production_rules():
        #                     for body in pr.get_bodys():
        #                         # print("bbd")
        #                         if body == b:
        #                             valid_productions[pr.get_variable()] = body
        #                             # print(pr.get_variable())
        #
        #
        #             # for k in valid_productions:
        #             #     x = []
        #             #     for d in valid_productions[k]:
        #             #         x.append(d.get_variable())
        #             #     print(k, x)
        #             print("----")
        #             print(valid_productions.keys())
        #             #
        #             # # find any valid productions
        #             # for b in bodys:
        #             #     for pr in self.get_grammar().get_production_rules():
        #             #         for body in pr.get_bodys():
        #             #             if body == b:
        #             #                 valid_productions[pr.get_variable()] = body
        #             #                 # valid_productions.append(ProductionRule(pr.get_variable(), body))
        #             #
        #
        #
        #         # remove overlap from valid productions
        #
        #
        #
        #
        #
        #
        #
        #         print("---")
        #
        #         #
        #         # # print(substr, end = "  ")
        #         # for k in valid_productions:
        #         #     if k == "aa":
        #         #         print(valid_productions["aa"])
        #
        #
        #
        #
        #



        # # generate parse table
        # parse_table = []
        # for i in range(0, len(string)):
        #     parse_table.append([])
        #     for j in range(0, len(string)-i):
        #         parse_table[i].append([])
        #
        # for i in range(0, len(string)):
        #     for j, substr in enumerate(self.__substrings(string, i+1)):
        #         # parse_table[i][j] = substr
        #
        #
        #         # calculate possible production rules
        #
        #         print("-------")
        #         strs = self.__splits(substr)
        #         for c in strs:
        #             print(c)
        #
        #         print("-------")
        #
        #
        #
        #
        #
        #
        #
        #         # print(parse_table[i-1], j)
        #         print(substr, i, " ", j)
        #         # print(j, substr, end = " ")
        #         # print("---")




            # print(self.__substrings(string, i))

        # for i in range(0, len(string)):
        #     for j in string
        #     print(i)


        # # base cases
        # for i, c in enumerate(string):
        #     for production_rule in self.get_grammar().get_production_rules():
        #         for j, body in enumerate(production_rule.get_bodys()):
        #             if [c] == body:
        #                 parse_table[0][i].append([production_rule, j])

        # recursive cases

        # print(parse_table)
        # for x in self.__splits([1,2,3,4]):
        #     print(x)
        #





        return parse_table

    def __splits(self, s):
        if len(s) == 1: return [s]
        return [[s[0:i+1], s[i+1:]] for i in range(0, len(s)-1)]

    def __substrings(self, string, l):
        return [string[i:i+l] for i in range(0, len(string)-l+1)]

    def __cartesian_product(self, A, B):
        return [[a[0],b[0]] for a in A for b in B]

    def __print_leftmost_derivation(self, string, parse_table):
        pass




