import sys
from DBProcessing import DBProcessing
from argument_parser import Parser

def main():
    parser = Parser()
    db = DBProcessing()

    known_args = parser.parse()
    db.connect(known_args)
if __name__ == "__main__":
    main()