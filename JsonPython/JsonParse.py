import json

book = {}

book['tom'] = {
    'name' : 'tom',
    'address' : '1, red street, NY',
    'number' : 123556
}

book['bob'] = {
    'name' : 'bob',
    'address' : '1, green street, NY',
    'number' : 788965
}

s = json.dumps(book)

with open('one.json', 'w') as f:
    f.write(s)