# pcost.py
#
# Exercise 1.27

import csv, sys

def portfolio_cost(filename):
    'Get total portfolio cost of a csv'

    total = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print('Something is not valid in row: ', row)

    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)