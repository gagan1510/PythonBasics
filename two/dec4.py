def new_decorator(func):
    def wrap_func():
        print('After this the func will get executed!')
        func()
        print('Code here will execute after func!')
    return wrap_func

@new_decorator #this is a decorator
def func_needs_dec():
    print('This function needs a decorator!')

#func_needs_dec = new_decorator(func_needs_dec) #the same thing here is done by the decorator!

func_needs_dec()

#the line number 13 modifies the func_needs_dec() and changes it in the way observed

# DECORATOR--> Take. Pass. Reassign.
