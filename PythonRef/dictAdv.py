d = {
    'fname' : 'Gaganpreet',
    'mname' : 'Singh',
    'lname' : 'kainth'
    }

# inserting into dictionary

d['city'] = 'jabalpur'

if 'fname' in d.keys():
    print("It is him")
else:
    print("It's not him")

print("\nThe dictionary is:\n")

del d['mname']

for key in d.keys():
    print(key, d[key])
