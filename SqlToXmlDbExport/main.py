import sys
import DBProcessing
import Parser

def main():
    parser = Parser()
    db = DBProcessing()

    args = parser.parse()