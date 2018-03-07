def reverse(text):
    return text[::-1]

def is_pal(text):
    if text == reverse(text):
        return True
    return False

text = input("Enter a string: ")
if is_pal(text):
    print("It's a pallindrome")

else:
    print("not a pallindrome")