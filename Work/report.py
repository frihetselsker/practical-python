# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Returns the list of sets with made of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                pass
    return prices


def make_report(portfolio, prices):
    '''Returns the list of dictionaries with entries made of a portfolio file'''
    report = []
    for stock in portfolio:
        stock['change'] = prices[stock['name']] - stock['price']
        stock['price'] = prices[stock['name']]
        report.append((stock['name'], stock['shares'], stock['price'], stock['change']))

    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- -----------')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$" + f"{price:0.2f}":>10s} {"$" + f"{change:0.2f}":>10s}')

    return report