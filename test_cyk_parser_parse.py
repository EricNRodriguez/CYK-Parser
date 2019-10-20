import unittest
import random
from cyk_parser import CYKParser

class TestCYKParserValidation(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCYKParserValidation, self).__init__(*args, **kwargs)
        self._output_file = open('output_test.txt', 'r+')
        self._cyk_parser = CYKParser('test_grammar.txt')

    def __check_for_word_in_output(self, word):
        return word in self._output_file.read()

    def test_empty_string(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("", self._output_file))

    def test_empty_string_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_number(self):
        self._output_file.truncate(0)
        n = random.randint(1, 1000)
        self.assertTrue(self._cyk_parser.parse(str(n) + ";", self._output_file))

    def test_number_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_number_without_semicolon(self):
        self._output_file.truncate(0)
        n = random.randint(1, 1000)
        self.assertFalse(self._cyk_parser.parse(str(n), self._output_file))

    def test_number_without_semicolon_REJECTED(self):
        self.assertTrue(self.__check_for_word_in_output("REJECTED"))

    def test_invalid_number(self):
        self._output_file.truncate(0)
        n = random.randint(1, 1000)
        self.assertFalse(self._cyk_parser.parse("0" + str(n) + ";", self._output_file))

    def test_invalid_number_REJECTED(self):
        self.assertTrue(self.__check_for_word_in_output("REJECTED"))

    def test_number_with_newline(self):
        self._output_file.truncate(0)
        n = '''
        12

        23  4
        ;

        '''
        self.assertTrue(self._cyk_parser.parse(n, self._output_file))

    def test_number_with_newline_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_invalid_symbol(self):
        self._output_file.truncate(0)
        self.assertFalse(self._cyk_parser.parse("letp=3;", self._output_file))

    def test_invalid_symbol_ERROR_INVALID_SYMBOL(self):
        self.assertTrue(self.__check_for_word_in_output("ERROR_INVALID_SYMBOL"))

    def test_simple_let_statement(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("letx=3;", self._output_file))

    def test_test_simple_let_statement_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))


    def test_invalid_operation_let_statement_(self):
        self._output_file.truncate(0)
        self.assertFalse(self._cyk_parser.parse("letx>3;", self._output_file))

    def test_invalid_operation_let_statement_REJECTED(self):
        self.assertTrue(self.__check_for_word_in_output("REJECTED"))

    def test_simple_plus_expression(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("(x>3);", self._output_file))

    def test_simple_plus_expression_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_simple_minus_expression(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("(x-3);", self._output_file))

    def test_simple_minus_expression_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_simple_mult_expression(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("(x*3);", self._output_file))

    def test_simple_mult_expression_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_simple_inequality_expression(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("(x>3);", self._output_file))

    def test_missing_opening_bracket_expression(self):
        self._output_file.truncate(0)
        self.assertFalse(self._cyk_parser.parse("x>3);", self._output_file))

    def test_missing_opening_bracket_expression_REJECTED(self):
        self.assertTrue(self.__check_for_word_in_output("REJECTED"))

    def test_missing_closing_bracket_expression(self):
        self._output_file.truncate(0)
        self.assertFalse(self._cyk_parser.parse("x>3);", self._output_file))

    def test_missing_closing_bracket_expression_REJECTED(self):
        self.assertTrue(self.__check_for_word_in_output("REJECTED"))

    def test_nested_let_expression(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("letx=(x+3);", self._output_file))

    def test_nested_let_expression_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_simple_while_do_nothing_statement(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("while(x>y)do;", self._output_file))

    def test_simple_while_do_nothing_statement_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_simple_while_do_let_statement(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("while(x>y)doletx=3;;", self._output_file))

    def test_simple_while_do_let_statement_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_missing_semicolon_while_do_let_statement(self):
        self._output_file.truncate(0)
        self.assertFalse(self._cyk_parser.parse("while(x>y)doletx=3;", self._output_file))

    def test_missing_semicolon_while_do_let_statement_REJECTED(self):
        self.assertTrue(self.__check_for_word_in_output("REJECTED"))

    def test_simple_while_do_nothing_else_nothing(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("while(x+3)doelse;", self._output_file))

    def test_simple_while_do_else_nothing_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_simple_while_do_something_else_nothing(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("while(x+3)doletx=3;else;", self._output_file))

    def test_simple_while_do_something_else_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))


    def test_simple_while_inequality_do_let_else_incrament(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("while(x>3)doletx=3;elseletx=(x+1);;",self._output_file))


    def test_simple_while_inequality_do_let_else_incrament_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_nested_while(self):
        self._output_file.truncate(0)
        self.assertTrue(self._cyk_parser.parse("while(x>3)dowhile(y+2)doletx=2;;;", self._output_file))

    def test_nested_while_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))

    def test_nested_while_missing_semicolon(self):
        self._output_file.truncate(0)
        self.assertFalse(self._cyk_parser.parse("while(x>3)dowhile(y+2)doletx=2;;", self._output_file))

    def test_nested_while_missing_semicolon_REJECTED(self):
        self.assertTrue(self.__check_for_word_in_output("REJECTED"))

    def test_nested_while_missing_expression(self):
        self._output_file.truncate(0)
        self.assertFalse(self._cyk_parser.parse("whiledowhile(y+2)doletx=2;;;", self._output_file))

    def test_nested_while_missing_expression_REJECTED(self):
        self.assertTrue(self.__check_for_word_in_output("REJECTED"))


    def test_nested_while_with_newline(self):
        self._output_file.truncate(0)
        string = '''
        
                    while
                    (x>3
                             )d 
                owhi
                         le(y   +2)do 
                    letx=2;;
                    
                    ;
                '''
        self.assertTrue(self._cyk_parser.parse(string, self._output_file))

    def test_nested_while_with_newline_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))


    def test_let_while(self):
        self._output_file.truncate(0)
        string = """
        letx=(y-
        20);whil  e
        \n 1doy;
    ;
        """
        self.assertTrue(self._cyk_parser.parse(string, self._output_file))

    def test_let_while_ACCEPTED(self):
        self.assertTrue(self.__check_for_word_in_output("ACCEPTED"))






if __name__ == '__main__':
    unittest.main()



