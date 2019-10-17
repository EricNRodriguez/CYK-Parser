from cyk_parser import CYKParser

def main():
    cyk_parser = CYKParser("hello.txt")
    #
    # string = parse_string("./test_file_path.txt")
    #
    cyk_parser.parse("seaFwaf")

    # cyk_parser.parse_grammar("hello.txt")


    return

if __name__ == '__main__':
    main()

