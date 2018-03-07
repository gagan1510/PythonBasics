#this ia program to show all the paths to the python language (3.5)

import  sys
import os
import this

print("The command line arguments are: ")
for i in sys.argv:
    print(i)

python_path = sys.path

print("The python path is:\n")
for i in python_path:
    print(i)

print("\n\n",os.getcwd()) #this will show the current directory of the project


#the list data structure

shop_list = ['apple', 'mangoes', 'carrot', 'banana']
print("I have ", len(shop_list), " items to buy.")
print("These items are:")
for item in shop_list:
    print(item, end = " ")

other = input("\n\nanything else to buy?")
if other != 'no':
    shop_list.append(other)
    print("The updated list is:")
    for item in shop_list:
        print(item, end=" ")

shop_list.sort()

print("The first item to be bought is:", shop_list[0])
old_item = []
old_item.append(shop_list[0])
del shop_list[0]

print(shop_list)