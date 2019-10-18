from sys import argv
from cyk_parser import CYKParser
from invalid_symbol_error import InvalidSymbolError

def main():

    if len(argv) < 3:
        print("Invalid number of arguments | requires file paths for grammar and string")
        quit()

    try:
        string = open(argv[2]).read().replace('\n', '').replace(" ", "")
    except FileNotFoundError as e:
        print("Invalid file path for string, does not exist")
        quit()
    except Exception as e:
        print(e.__repr__())
        quit()

    try:
        cyk_parser = CYKParser(argv[1])
    except FileNotFoundError as e:
        print("Invalid file path for grammar, does not exist")
        quit()
    except Exception as e:
        print(e.__repr__())
        quit()

    try:
        print("ACCEPTED") if cyk_parser.parse(string) else print("REJECTED")
    except InvalidSymbolError as e:
        print(e.__str__())
        quit()
    except Exception as e:
        print(e.__repr__())
        quit()


if __name__ == '__main__':
    main()

