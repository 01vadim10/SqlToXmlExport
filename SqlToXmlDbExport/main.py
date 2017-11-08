import sys
import DBProcessing
import argument_parser

def main():
    parser = Parser()
    db = DBProcessing()

    args = parser.parse()