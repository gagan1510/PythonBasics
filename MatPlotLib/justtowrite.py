import urllib.request

u = urllib.request.urlopen('https://pythonprogramming.net/yahoo_finance_replacement').read().decode()

f = open('Adjus.txt', 'w')

stock = u.split(' ')

for line in stock:
    f.write(line)