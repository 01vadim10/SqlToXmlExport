import argparse

ap = argparse.ArgumentParser(description='Just an example')
ap.add_argument('who', nargs='?', default='World')
ap.add_argument('-db', '--database', action='store_true')
ns = ap.parse_args()
if ns.db:
    greet = 'Most falicitous salutations, o {}.'
else:
    greet = 'Hello, {}!'
print(greet.format(ns.who))