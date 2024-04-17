# Create table by tabulate library
# Install package tabulate first
# python -m pip install tabulate

from tabulate import tabulate

data = [['Ploy', 35000], ['Top', 50000]]
header = ['name', 'salary']

print(tabulate(data, header))