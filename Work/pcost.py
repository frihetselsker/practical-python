# pcost.py
#
# Exercise 1.27
import csv, sys

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as file:
        rows = csv.reader(file)
        next(rows) # to remove the headers
        for row in rows:
            t = (row[0], int(row[1]), float(row[2]))
            try:
                total_cost += t[1] * t[2]
            except ValueError:
                print("Error: invalid file structure. Please, make changes to avoid this error")
                exit()
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)