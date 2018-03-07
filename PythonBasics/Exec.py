exec("print('so this is inside exec!')")

list_str = "[1,2,3,4,5,6,7,8,9]"
list_str = exec(list_str)
print(list_str)

exec("list_str2 = [1,3,4,5,6,7]")
print(list_str2)

exec("def test(): print('down d-d down down')")
test()

exec("""
def test2():
    print('Lets see if multi line works with exec')
""")

test2()