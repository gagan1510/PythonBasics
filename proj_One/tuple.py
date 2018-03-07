# tuples are inside ( ) and can have another pair inside the parent pair
# just like the 2D array is initialized
#here, zoo is the tuple

zoo = ("monkey", "lion", "wolf")
new_zoo = "zebra", "donkey", zoo
print(new_zoo)

#NOTE that the zoo will be inside () inside the new_zoo parent parenthesis

print(len(new_zoo))

print("\n")

#NOTE that the () inside the parent brackets are taken as a single entity and the length here will be 3

# DICTIONARIES in python

myDict = {'gagan': 'gaganpreet.gs007@gmail.com',
          'mark': 'marktwinson@hotmail.com',
          'Larry': 'larry@wall.org',
          'Matsumoto': 'matz@ruby-lang.org',
          'Spammer': 'spammer@hotmail.com'
          }

for name, mail in myDict.items():
    print("The name is {} and e-mail id is: {}".format(name, mail))

#adding a key value pair

#add_key = input("enter the key to be added: ")
#add_mail = input("enter it's e-mail address: ")

#myDict[add_key] = add_mail
#print("\nThe updated dictionary is: \n")
#for name, mail in myDict.items():
#    print("The name is {} and e-mail id is: {}".format(name, mail))

new_list = [1,2,3,4,5,6,7,8,9,10]
print(new_list)
#now to print individual elements of the list
for ele in new_list:
    print(ele, end=", ")

print("\n")
#now, to print a list in reverse order
print(new_list[::-1])

# new_list[a::b] starts from a goes to b-1 but stops at b

# SETS
set_one = set(["ele1", "ele2", "ele3"])
is_there = "ele1" in set_one
print(is_there, "ele1 is there")
is_there = "ele4" in set_one
print(is_there, " ele4 is there")

set_two = set_one.copy()
set_two.add("ele4")

is_there2 = "ele4" in set_one
is_superset = set_two.issuperset(set_one)
print(is_superset, " shows superset")

print(set_one & set_two) #this shows elements present in both the sets