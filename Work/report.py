# report.py
#
# Exercise 2.4

import stock, tableformat
from fileparse import parse_csv

def read_portfolio(filename):
    'Create list of stocks from csv'

    with open(filename) as file:
        portdicts = parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float])

    portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]

    return portfolio

def read_prices(filename):
    'Create dict from csv'
    
    with open(filename) as file:
        prices = { name: price for name, price in parse_csv(file, types=[str, float], has_headers=False) }

    return prices

def portfolio_cost(portfolio):
    'Get total portfolio cost'

    cost = 0

    for holding in portfolio:
        cost += holding.shares * holding.price

    return cost  

def current_value(portfolio, prices):
    'Get current value of portfolio'

    current_value = 0

    for holding in portfolio:
        if holding.name in prices:
            current_value += holding.shares * prices[holding.name]

    return current_value

def make_report_data(portfolio, prices):
    'Generate report'

    report = []

    for holding in portfolio:
        if holding.name in prices:
            report.append((
                holding.name, 
                holding.shares, 
                prices[holding.name],
                prices[holding.name] - holding.price
            ))

    return report

def print_report(reportdata, formatter):
    formatter.headings(['Name','Shares','Price','Change'])

    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:>0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfile, pricefile, fmt='txt'):
    reportdata = make_report_data(read_portfolio(portfile), read_prices(pricefile))
    formatter = tableformat.create_formatter(fmt)
    print_report(reportdata, formatter)

def main(argv):
    if len(argv) < 3 or len(argv) > 4:
        print(f'Usage: {argv[0]} portfile pricefile [output_format]')
    elif len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    else:
        portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)