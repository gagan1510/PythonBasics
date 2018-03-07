import string

form1 = """\
Dear %(name)s,
Please send me back my %(item)s or pay me $%(amount)0.2f.
                    
                        Sincerely yours,
                        A python User
"""

print(form1 % {'name' : 'Mr. Deadpool',
              'item' : 'blender',
              'amount' : 50.50,
              })

form2 = string.Template("""\
Dear $name,
Please send me back my $item or pay me $amount.
                    
                        Sincerely yours,
                        A python User
"""
)

prhelp = {'name' : 'Gagan',
          'item' : 'blender',
          'amount' : "%0.2f" % 50.0}
print(form2.substitute(prhelp)) # this takes a dictionary of replacements

