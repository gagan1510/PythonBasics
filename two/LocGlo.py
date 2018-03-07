# the globals() and locals() return the dictionary containing the name of variables as keys and their values as items

s = 'This is a Global variable!'

def func():
    m = 'This is a local variable of func!'
    print(locals()['m'])
    return

print(globals()['s'])
func()