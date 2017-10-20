#import argparse

#ap = argparse.ArgumentParser(description='Export Database from SQL Server to Xml-file')
#ap.add_argument('db', required=True)
#ap.add_argument('-v', '--verbose', action='store_true')
#ns = ap.parse_args()
#if ns.db:
#    connectionString = ns.db

#else:
#    greet = 'Hello, {}!'
#print(greet.format(ns.who))

from argparse import ArgumentParser

class Parser(object):
    """Argument parser that can handle arguments with our database connection.

    """

    def __init__(self):
        self._parser = ArgumentParser(prog='ScoiX', description='Sql conversion operation in Xml')
        self._add_arguments()

    def _add_arguments(self):
        """Adds arguments to parser."""
        self._parser.add_argument(
            '-srv', '--server',
            action='store_true',
            help="enter server name")
        self._parser.add_argument(
            '-db', '--database',
            nargs='?',
            const=get_alias(),
            help='enter database name')
        self._parser.add_argument(
            '-u', '--username',
            action='store_true',
            help='enter username')
        self._parser.add_argument(
            '-p', '--password',
            action='store_true',
            help='enter password')
        self._parser.add_argument(
            '-h', '--help',
            action='store_true',
            help='show this help message and exit')

    def parse(self):
        return self._parser.parse_args()
