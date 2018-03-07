from collections import Counter

# the counter function counts the number of occurrences of each of the members of a list

l = [1,1,1,1,2,3,3,3,3,4,5,5,5,5,5,6,7,8,9,7,6,6,6,6]

x = Counter(l)

for k in x:
    print("{} : {}".format(k , x[k]))

# here, x is a dictionary containing the element as key and their count as items/values

print("\n")

s = "my name is gagan preet singh kainth"
s2 = Counter(s)

for k in s2:
    print("{} : {}".format(k , s2[k]))

# to count the number of words in a string

print("\n")

st = "gagan gagan preet singh kainth kainth kainth kainth"
sp = st.split()

count_wd =Counter(sp)

for k in count_wd:
    print("{} : {}".format(k, count_wd[k]))

# the most_common() returns the list of tuples containing the most occurring words

print("\n")

most_count = count_wd.most_common(2)

print(most_count)

print("\n")

print("The total number of words are : ", sum(count_wd.values()))

