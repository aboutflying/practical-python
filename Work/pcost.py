# pcost.py
#
# Exercise 1.27

import csv
from report import read_portfolio

def portfolio_cost(filename):
    'Get total portfolio cost of a csv'

    total = sum([s['price']*s['shares'] for s in read_portfolio(filename)])

    return total

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    print('Total cost', portfolio_cost(filename))


if __name__ == '__main__':
    import sys
    main(sys.argv)