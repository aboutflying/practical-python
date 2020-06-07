# report.py
#
# Exercise 2.4

import csv, locale
from fileparse import parse_csv

locale.setlocale(locale.LC_ALL, '')

def read_portfolio(filename):
    'Create list of dicts from csv'

    portfolio = parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])

    return portfolio

def read_prices(filename):
    'Create dict from csv'
    
    prices = { name: price for name, price in parse_csv(filename, types=[str, float], has_headers=False) }

    return prices

def portfolio_cost(portfolio):
    'Get total portfolio cost'

    cost = 0

    for holding in portfolio:
        cost += holding['shares'] * holding['price']

    return cost  

def current_value(portfolio, prices):
    'Get current value of portfolio'

    current_value = 0

    for holding in portfolio:
        if holding['name'] in prices:
            current_value += holding['shares'] * prices[holding['name']]

    return current_value

def make_report(portfolio, prices):
    'Generate report'

    report = []

    for holding in portfolio:
        if holding['name'] in prices:
            report.append((
                holding['name'], 
                holding['shares'], 
                prices[holding['name']], 
                prices[holding['name']] - holding['price']
            ))

    return report

def print_report(report):
    headers = ('Name','Shares','Price','Change')

    print('%10s %10s %10s %10s'% headers)
    print(('-' * 10 + ' ') * len(headers))

    for name, shares, price, change in report:
        price = locale.currency(price)
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10,.2f}')

    print('\n')
    
def portfolio_report(portfolio_filename="Data/portfolio.csv", prices_filename="Data/prices.csv"):
    report = make_report(read_portfolio(portfolio_filename), read_prices(prices_filename))
    print(f'{portfolio_filename:*^43s}')
    print_report(report)

def main(argv):
    if len(argv) > 1:
        for file in argv[1:]:
            portfolio_report(file)
    else:
        portfolio_report()

if __name__ == '__main__':
    import sys
    main(sys.argv)